from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.forms import SearchForm, ProjectForm, ProjectUsersForm
from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    ordering = ['-start_date']
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) |
                Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.filter(is_deleted=False).order_by('-created_at')
        context['is_member'] = self.object.is_member(self.request.user)
        return context


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_project'
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.users.add(self.request.user)
        return response

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_project'
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_update.html'

    def has_permission(self):
        return super().has_permission() and self.get_object().is_member(self.request.user)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_project'
    model = Project
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('index')

    def has_permission(self):
        return super().has_permission() and self.get_object().is_member(self.request.user)


class ProjectUsersUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_project_users'
    model = Project
    form_class = ProjectUsersForm
    template_name = 'project/project_users.html'

    def has_permission(self):
        return super().has_permission() and self.get_object().is_member(self.request.user)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
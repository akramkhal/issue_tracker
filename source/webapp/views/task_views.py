from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskDetailView(DetailView):
    template_name = 'task/task_detail.html'

    def get_queryset(self):
        return Task.objects.filter(is_deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_member'] = self.object.project.is_member(self.request.user)
        return context


class TaskCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_task'
    model = Task
    form_class = TaskForm
    template_name = 'task/task_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def has_permission(self):                              # ← new
        return super().has_permission() and self.project.is_member(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def form_valid(self, form):
        form.instance.project = self.project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.project.pk})


class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_task'
    form_class = TaskForm
    template_name = 'task/task_update.html'

    def get_queryset(self):
        return Task.objects.filter(is_deleted=False)

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().project.is_member(self.request.user)


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_task'
    template_name = 'task/task_delete.html'

    def get_queryset(self):
        return Task.objects.filter(is_deleted=False)

    def form_valid(self, form):
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().project.is_member(self.request.user)
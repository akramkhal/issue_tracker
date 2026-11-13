from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView, CreateView

from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskDetailView(TemplateView):
    template_name = 'task/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def form_valid(self, form):
        form.instance.project = self.project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.project.pk})


class TaskUpdateView(View):
    template_name = 'task/task_update.html'

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(instance=task)
        return render(request, self.template_name, {'form': form, 'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, self.template_name, {'form': form, 'task': task})


class TaskDeleteView(View):
    template_name = 'task/task_delete.html'

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, self.template_name, {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        project_pk = task.project.pk
        task.delete()
        return redirect('project_detail', pk=project_pk)
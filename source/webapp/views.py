from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from webapp.models import Task
from webapp.forms import TaskForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all().order_by('-created_at')
        return context


class TaskDetailView(TemplateView):
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskCreateView(View):
    template_name = 'task_create.html'

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)

        if form.is_valid():
            if form.is_valid():
                task = form.save()
                return redirect('task_detail', pk=task.pk)

        return render(request, self.template_name, {'form': form})


class TaskUpdateView(View):
    template_name = 'task_update.html'

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
    template_name = 'task_delete.html'

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, self.template_name, {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')

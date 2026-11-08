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
            summary = form.cleaned_data.get('summary')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            task_type = form.cleaned_data.get('type')
            task = Task.objects.create(summary=summary, description=description,
                                       status=status, type=task_type)
            return redirect('task_detail', pk=task.pk)

        return render(request, self.template_name, {'form': form})

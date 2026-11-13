from django.views.generic import ListView

from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    ordering = ['-start_date']
    paginate_by = 5
    paginate_orphans = 1


from django.urls import path
from webapp.views import (IndexView, TaskDetailView, TaskCreateView, TaskUpdateView,
                          TaskDeleteView, ProjectListView, ProjectDetailView)

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('tasks/', IndexView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('add_task/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]
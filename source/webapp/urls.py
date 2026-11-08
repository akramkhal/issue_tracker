from django.urls import path
from webapp.views import IndexView, TaskDetailView, TaskCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('add_task/', TaskCreateView.as_view(), name='task_create'),
]
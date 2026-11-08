from django.contrib import admin
from webapp.models import Task, TaskType, TaskStatus


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('id', 'summary', 'status', 'type', 'created_at', 'updated_at')
    list_filter = ('status', 'type')
    search_fields = ('summary',)


@admin.register(TaskType)
class TaskType(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(TaskStatus)
class TaskStatus(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

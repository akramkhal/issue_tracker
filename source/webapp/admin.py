from django.contrib import admin
from webapp.models import Task, TaskType, TaskStatus


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'types')
    search_fields = ('summary',)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

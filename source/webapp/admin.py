from django.contrib import admin
from webapp.models import Task, TaskType, TaskStatus, Project


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'status', 'project', 'created_at', 'updated_at')
    list_filter = ('status', 'types', 'project')
    search_fields = ('summary',)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date')
    list_filter = ('start_date',)
    search_fields = ('name', 'description')

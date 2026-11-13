from django.db import models
from webapp.validators import validate_capitalized, validate_min_length


class Task(models.Model):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Краткое описание',
                               validators=[validate_capitalized])
    description = models.TextField(null=True, blank=True, verbose_name='Полное описание',
                                   validators=[validate_min_length])
    status = models.ForeignKey('webapp.TaskStatus', on_delete=models.PROTECT, related_name='tasks', verbose_name='Статус')
    types = models.ManyToManyField('webapp.TaskType', related_name='tasks', verbose_name='Типы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, related_name='tasks',
                                verbose_name='Проект')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалена')

    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class TaskType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class TaskStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Project(models.Model):
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

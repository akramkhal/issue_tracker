from django import forms
from webapp.models import TaskStatus, TaskType


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}), label='Краткое описание')
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                                  label='Полное описание')
    status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-select'}), label='Статус',
                                    empty_label='--Выберите статус--')
    types = forms.ModelMultipleChoiceField(queryset=TaskType.objects.all(),
                                                       widget=forms.CheckboxSelectMultiple(), label='Типы')

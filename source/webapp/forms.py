from django import forms
from webapp.models import Task


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти',
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Название или описание'}))


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types']
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'types': forms.CheckboxSelectMultiple(),
        }


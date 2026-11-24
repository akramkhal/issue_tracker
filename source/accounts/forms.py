from django import forms
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise forms.ValidationError('Заполните хотя бы одно из полей: имя или фамилия.')
        return cleaned_data
from django import forms
from .models import Task

class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', 'deadline'] # , 'status']
        widgets = {
            'deadline':forms.DateInput(attrs={'type':'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        if len(title) < 3 and len(title) >= 200:
            self.add_error('title', 'El título debe tener al menos 3 caracteres')

        return cleaned_data

class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', 'deadline', 'status']
        widgets = {
            'deadline':forms.DateInput(attrs={'type':'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        if len(title) < 3 and len(title) >= 200:
            self.add_error('title', 'El título debe tener al menos 3 caracteres')

        return cleaned_data
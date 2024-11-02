from django import forms
from .models import Task

class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority']
        widgets = {
            'deadline':forms.DateInput(attrs={'type':'date'}),
        }
        error_messages  = {
            'title': {
                'min_length': "El título debe tener al menos 3 caracteres.",            
                'max_length': "El título debe tener máximo 200 caracteres.",
            },
            'description': {
                'min_length': "La descripción debe tener al menos 3 caracteres.",            
                'max_length': "El título debe tener máximo 200 caracteres.",
            },
        }

class TaskUpdateForm(forms.ModelForm):

    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Completada"
    )

    deadline = forms.DateField(
        input_formats=['%m-%d-%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'}),
        label = "Fecha límite"
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline','priority', 'status']
        error_messages  = {
            'title': {
                'min_length': "El título debe tener al menos 3 caracteres.",            
                'max_length': "El título debe tener máximo 200 caracteres.",
            },
            'description': {
                'min_length': "La descripción debe tener al menos 3 caracteres.",            
                'max_length': "El título debe tener máximo 200 caracteres.",
            },
        }
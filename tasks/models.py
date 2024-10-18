from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    PRIORITY = {
        'Baja':'Baja',
        'Media':'Media',
        'Alta':'Alta',
    }

    STATUS = {
         'Completada':'Completada',
         'En Progreso':'En Progreso',
    }
    
    title = models.CharField(validators=[MinLengthValidator(3)], max_length=200, verbose_name="Título")
    description = models.TextField(max_length=200, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    deadline = models.DateField(verbose_name="Fecha límite")
    priority = models.CharField(max_length=12, choices=PRIORITY, blank=True, default='Baja', verbose_name="Prioridad")
    status = models.CharField(max_length=12, choices=STATUS, blank=True, default='En Progreso', verbose_name="Estado")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('task', args=[str(self.id)])

    def __str__(self) -> str:
        return self.title
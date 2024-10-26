from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    PRIORITY = {
        ('B','Baja'),
        ('M','Media'),
        ('A','Alta'),
    }
    
    title = models.CharField(validators=[MinLengthValidator(3)], max_length=50, verbose_name="Título")
    description = models.TextField(validators=[MinLengthValidator(3)], max_length=200, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    deadline = models.DateField(verbose_name="Fecha límite")
    priority = models.CharField(max_length=1, choices=PRIORITY, blank=True, default='B', verbose_name="Prioridad")
    status = models.BooleanField(default=False, verbose_name="Completada")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('task', args=[str(self.id)])

    def __str__(self) -> str:
        return self.title
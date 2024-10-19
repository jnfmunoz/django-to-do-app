from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    PRIORITY = {
        ('B','Baja'),
        ('M','Media'),
        ('A','Alta'),
    }

    STATUS = {
         ('E','En Progreso'),
         ('C','Completada'),
    }
    
    title = models.CharField(validators=[MinLengthValidator(3)], max_length=200, verbose_name="Título")
    description = models.TextField(max_length=200, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    deadline = models.DateField(verbose_name="Fecha límite")
    priority = models.CharField(max_length=1, choices=PRIORITY, blank=True, default='B', verbose_name="Prioridad")
    status = models.CharField(max_length=12, choices=STATUS, blank=True, default='E', verbose_name="Estado")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('task', args=[str(self.id)])

    def __str__(self) -> str:
        return self.title
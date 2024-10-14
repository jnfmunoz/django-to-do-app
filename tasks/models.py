from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.model):
    titulo = models.CharField(min_length=100 ,max_length=200)
    descripcion = models.TextField(min_length=100 ,max_length=200)
    fecha_limite = models.DateField()
    prioridad = models.CharField()
    estado = models.BooleanField(default=False)
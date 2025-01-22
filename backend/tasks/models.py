from django.db import models

# Create your models here.

class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    hecho = models.BooleanField(default=False)
    creacion = models.DateField(auto_now_add=True)

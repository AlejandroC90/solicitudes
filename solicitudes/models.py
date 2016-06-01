from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.forms import ModelForm
# Create your models here.

class Solicitud(models.Model):
    codigo = models.IntegerField(blank=False,null=False)
    nombre = models.CharField(max_length=50)
    tipo_solicitud = models.TextField(blank=False)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    adjunto = models.FileField(default=False)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=20,default='Pendiente')

    def __str__(self):
        return  '%s  %s ' %(str(self.codigo), ' - Estado: ' + self.estado)



class Informe(models.Model):
    fecha_creacion = models.DateTimeField(blank=False)
    accion = models.TextField(max_length=200)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=10, null=False,default=0)

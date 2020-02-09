from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MaterialDeEstudio(models.Model):
    sede = models.CharField(max_length=20, default='Bogota')
    titulo = models.CharField(max_length=30)
    semestre = models.CharField(max_length=30)
    facultad = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)
    docente= models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.titulo}"


class Parcial(MaterialDeEstudio):
    imagen = models.ImageField(upload_to='images/parciales')


class Talleres(MaterialDeEstudio):
    imagen = models.ImageField(upload_to='images/talleres')


class Apuntes(MaterialDeEstudio):
    archivo = models.FileField(upload_to='images/apuntes')
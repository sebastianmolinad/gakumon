from django.db import models

# Create your models here.
class MaterialDeEstudio(models.Model):
    sede = models.CharField(max_length=20, default='Bogota')
    titulo = models.CharField(max_length=30)
    semestre = models.CharField(max_length=30)
    facultad = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)
    docente = models.CharField(max_length=30)
    class Meta:
        abstract = True

class Parcial(MaterialDeEstudio):
    imagen = models.ImageField(upload_to='images/')

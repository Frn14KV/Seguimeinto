from django.db import models


# Create your models here.
class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=50)
    descripcion_carrera = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre_carrera

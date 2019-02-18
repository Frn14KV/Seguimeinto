from django.db import models


# Create your models here.
class AreaConocimiento(models.Model):
    nombre_area = models.CharField(max_length=50)
    descripcion_area = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre_area

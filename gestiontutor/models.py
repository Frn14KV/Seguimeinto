from django.db import models
from gestioncarrera.models import Carrera


# Create your models here.
class Tutor(models.Model):
    nombre_tutor = models.CharField(max_length=50)
    apellido_tutor = models.CharField(max_length=50)
    correo_tutor = models.EmailField()
    cedula_tutor = models.CharField(max_length=10)
    telefono_tutor = models.CharField(max_length=20)
    imagen_tutor = models.ImageField(upload_to="tutores/perfiles/", null=True, blank=True)
    Carrera_tutor = models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_tutor

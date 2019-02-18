from django.db import models
from gestioncarrera.models import Carrera


# Create your models here.
class Autor(models.Model):
    nombre_autor = models.CharField(max_length=50)
    apellido_autor = models.CharField(max_length=50)
    cedula_autor = models.CharField(max_length=10)
    correo_autor = models.EmailField()
    telefono_autor = models.CharField(max_length=20)
    imagen_autor = models.ImageField(upload_to="autores/perfiles/", null=True, blank=True)
    Carrera_autor = models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_autor





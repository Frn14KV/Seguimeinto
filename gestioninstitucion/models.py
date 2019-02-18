from django.db import models

# Create your models here.
class Institucion(models.Model):
    nombre_institucion = models.CharField(max_length=50)
    direccion_institucion = models.CharField(max_length=60)
    correo_institucion = models.EmailField()
    telefono_institucion = models.CharField(max_length=20)
    descripcion_institucion = models.TextField(max_length=200)
    imagen_institucion = models.ImageField(upload_to="instituciones/", null=True, blank=True)

    def __str__(self):
        return self.nombre_institucion

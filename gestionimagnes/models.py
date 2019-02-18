from django.db import models
from gestionproyecto.models import Proyecto

# Create your models here.
class Imagenes(models.Model):
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
    nombre_imagenes = models.FileField(upload_to="proyectos/imagenes/", null=True, blank=True)




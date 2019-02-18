from django.db import models
from gestionproyecto.models import Proyecto

# Create your models here.
class Archivos(models.Model):
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
    nombre_archivos = models.FileField(upload_to="proyectos/archivos/", null=True, blank=True)

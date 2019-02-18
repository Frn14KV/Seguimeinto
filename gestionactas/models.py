from django.db import models
from gestionproyecto.models import Proyecto

# Create your models here.
class Actas(models.Model):
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
    nombre_actas =models.FileField(upload_to="proyectos/actas/", null=True, blank=True)

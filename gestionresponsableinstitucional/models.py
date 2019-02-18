from django.db import models
from gestioninstitucion.models import Institucion


# Create your models here.
class ResponsableInstitucional(models.Model):
    nombre_responsable = models.CharField(max_length=20)
    apellido_responsable = models.CharField(max_length=50)
    correo_responsable = models.CharField(max_length=40)
    telefono_responsable = models.CharField(max_length=20)
    imagen_responsable = models.ImageField(upload_to="responsableinstitucional/perfiles/", null=True, blank=True)
    Institucion = models.ForeignKey(Institucion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        mensaje = self.nombre_responsable
        return mensaje

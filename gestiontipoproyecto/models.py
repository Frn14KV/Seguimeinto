from django.db import models


# Create your models here.
class TipoProyecto(models.Model):
    nombre_tipo = models.CharField(max_length=50)
    descripcion_tipo = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre_tipo

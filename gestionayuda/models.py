from django.db import models
# Create your models here.
class Ayuda(models.Model):
    nombre =models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre

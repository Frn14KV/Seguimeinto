from django.db import models
# Create your models here.
class Ayuda4(models.Model):
    nombre4 =models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre4

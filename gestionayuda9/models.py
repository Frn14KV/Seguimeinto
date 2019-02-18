from django.db import models
# Create your models here.
class Ayuda9(models.Model):
    nombre9 =models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre9

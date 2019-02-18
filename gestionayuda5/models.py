from django.db import models
# Create your models here.
class Ayuda5(models.Model):
    nombre5 =models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre5

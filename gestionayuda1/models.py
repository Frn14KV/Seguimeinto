from django.db import models
# Create your models here.
class Ayuda1(models.Model):
    nombre1 =models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre1

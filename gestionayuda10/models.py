from django.db import models
# Create your models here.
class Ayuda10(models.Model):
    email1 = models.EmailField()

    def __str__(self):
        return self.email1

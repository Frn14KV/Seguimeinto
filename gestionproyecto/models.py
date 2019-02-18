from django.db import models
from gestionautor.models import Autor
from gestiontutor.models import Tutor
from gestionresponsableinstitucional.models import ResponsableInstitucional
from gestioninstitucion.models import Institucion
from gestiontipoproyecto.models import TipoProyecto
from gestionareaconocimiento.models import AreaConocimiento

# Create your models here.
class Proyecto(models.Model):
    #Datos Generales
    Titulo = models.CharField(max_length=70)
    Institucion = models.ManyToManyField(Institucion)
    TipoProyecto = models.ManyToManyField(TipoProyecto)
    Proposito = models.TextField(max_length=300)
    ResponsableInstitucional = models.ManyToManyField(ResponsableInstitucional)
    Tutor = models.ManyToManyField(Tutor)
    Autor = models.ManyToManyField(Autor)
    AreaConocimiento = models.ManyToManyField(AreaConocimiento)

    #Datos Especificos
    Estado_proyecto = models.CharField(max_length=50, null=True)
    Poblacion_utiliza = models.CharField(max_length=30, null=True)
    Numero_muestra_ninos = models.CharField(max_length=30, null=True)
    Donado = models.CharField(max_length=5, null=True)
    Fecha_Donacion=models.DateTimeField(auto_now_add=False, null=True)
    Tiempo_inactividad = models.CharField(max_length=50, null=True)
    Sugerencias = models.CharField(max_length=50, null=True)


    def __str__(self):
        mensaje = (str("Proyecto con los ") + str(self.Titulo) + str(self.Tutor)  + str(self.Autor) + str("a sido registrado con exito"))
        return mensaje

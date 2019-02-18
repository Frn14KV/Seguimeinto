from django import forms
from gestionproyecto.models import Proyecto


class GuardarProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['Titulo',
                  'Institucion',
                  'TipoProyecto',
                  'Proposito',
                  'ResponsableInstitucional',
                  'Tutor',
                  'Autor',
                  'AreaConocimiento',
                  'Estado_proyecto',
                  'Poblacion_utiliza',
                  'Numero_muestra_ninos',
                  'Donado',
                  'Fecha_Donacion',
                  'Tiempo_inactividad',
                  'Sugerencias',]
        labels = {'Titulo':'Titulo del Proyecto:',
                  'Proposito': 'Proposito del Proyecto:',
                  'Estado_proyecto': 'Estado del Proyecto:',
                  'Poblacion_utiliza': 'Poblacion que utiliza el Proyecto:',
                  'Numero_muestra_ninos': 'Numero de muestra de ninos para el Proyecto:',
                  'Fecha_Donacion':'Fecha de Donacion(mes/dia/anio)',
                  'Tiempo_inactividad': 'Tiempo de inactividad del Proyecto:',
                  'Sugerencias': 'Sugerencias del Proyecto:',}
        widgets = {'Titulo':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: Sam'}),
                   'Proposito': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Es para fines educativos'}),
                   'Estado_proyecto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Nuevo'}),
                   'Poblacion_utiliza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Una Escuela'}),
                   'Numero_muestra_ninos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 15'}),
                   'Fecha_Donacion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 03/03/2018','type':'date'}),
                   'Tiempo_inactividad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 6 meses'}),
                   'Sugerencias': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Se puede utilizar python'}),}

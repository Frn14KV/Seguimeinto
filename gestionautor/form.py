from django import forms
from gestionautor.models import Autor


class GuardarAutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre_autor',
                  'apellido_autor',
                  'cedula_autor',
                  'correo_autor',
                  'telefono_autor',
                  'imagen_autor',
                  'Carrera_autor',]
        labels = {'nombre_autor':'Nombre:',
                  'apellido_autor':'Apellido:',
                  'cedula_autor': 'No. Cedula:',
                  'correo_autor':'Correo:',
                  'telefono_autor':'Telefono:'}
        widgets = {'cedula_autor': forms.NumberInput(attrs={'class': 'form-control','name':'cedula_autor','placeholder': 'Ejemplo: 01020304050','type':'number'}),
                   'nombre_autor':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: Ricardo'}),
                   'apellido_autor': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: Carrion'}),
                   'telefono_autor': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: 072145698 o 0991425368'}),
                   'correo_autor': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: carrion@hotmail.com','type':'email'}),}



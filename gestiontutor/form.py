from django import forms
from gestiontutor.models import Tutor


class GuardarTutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nombre_tutor',
                  'apellido_tutor',
                  'cedula_tutor',
                  'correo_tutor',
                  'telefono_tutor',
                  'imagen_tutor',
                  'Carrera_tutor',]
        labels = {'cedula_tutor':'No. Cedula:',
                  'nombre_tutor':'Nombre:',
                  'apellido_tutor':'Apellido:',
                  'correo_tutor':'Correo:',
                  'telefono_tutor':'Telefono:'}
        widgets = {'cedula_tutor': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: 05040302010','type':'number'}),
                   'nombre_tutor':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: Armando'}),
                   'apellido_tutor': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: Parra'}),
                   'telefono_tutor': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: 078963214 o 0998765321'}),
                   'correo_tutor': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: parra@gmail.com','type':'email'}),}

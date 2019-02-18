from django import forms
from gestionresponsableinstitucional.models import ResponsableInstitucional


class GuardarResponsableForm(forms.ModelForm):
    class Meta:
        model = ResponsableInstitucional
        fields = ['nombre_responsable',
                  'apellido_responsable',
                  'correo_responsable',
                  'telefono_responsable',
                  'imagen_responsable',
                  'Institucion',]
        labels = {'nombre_responsable':'Nombre:',
                  'apellido_responsable':'Apellido:',
                  'correo_responsable':'Correo:',
                  'telefono_responsable':'Telefono:'}
        widgets = {'nombre_responsable':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: Juan'}),
                   'apellido_responsable': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: Rolan'}),
                   'telefono_responsable': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: 072369854 o 0987654321'}),
                   'correo_responsable': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: juan@outlook.com','type':'email'}),}

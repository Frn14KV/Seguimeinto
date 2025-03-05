from django import forms
from gestioninstitucion.models import Institucion

class GuardarInstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre_institucion',
                  'direccion_institucion',
                  'correo_institucion',
                  'telefono_institucion',
                  'imagen_institucion',
                  'descripcion_institucion',]
        labels = {'nombre_institucion':'Nombre:',
                  'direccion_institucion':'Direccion:',
                  'correo_institucion':'Correo:',
                  'telefono_institucion':'Telefono:',
                  'descripcion_institucion': 'Descripcion:'}
        widgets = {'nombre_institucion':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: UPS'}),
                   'direccion_institucion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: Av. Europa.'}),
                   'telefono_institucion': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: 0723654789 o 0987654321'}),
                   'correo_institucion': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: abc@outlook.com','type':'email'}),
                   'descripcion_institucion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: La Institución se dedica al apoyo de la sociedad.'}),}

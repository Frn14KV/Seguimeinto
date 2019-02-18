from django import forms
from gestioncarrera.models import Carrera


class GuardarCarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre_carrera',
                  'descripcion_carrera',]
        labels = {'nombre_carrera':'Nombre:',
                  'descripcion_carrera':'Descripcion:',}
        widgets = {'nombre_carrera':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: Ingenieria de Sistemas.'}),
                   'descripcion_carrera': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Ejemplo: Esta carrera se oferta en la UPS.'}),}

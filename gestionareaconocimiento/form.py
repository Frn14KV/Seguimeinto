#franklin
from django import forms
from gestionareaconocimiento.models import AreaConocimiento


class GuardarAreaForm(forms.ModelForm):
    class Meta:
        model = AreaConocimiento
        fields = ['nombre_area',
                  'descripcion_area',]
        labels = {'nombre_area':'Nombre:',
                  'descripcion_area':'Descripcion:',}
        widgets = {'nombre_area':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: Matematicas.'}),
                   'descripcion_area': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Ejemplo: Esta es una area basica de estudio.'}),}

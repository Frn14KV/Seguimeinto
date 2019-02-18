from django import forms
from gestiontipoproyecto.models import TipoProyecto


class GuardarTipoForm(forms.ModelForm):
    class Meta:
        model = TipoProyecto
        fields = ['nombre_tipo',
                  'descripcion_tipo',]
        labels = {'nombre_tipo':'Nombre:',
                  'descripcion_tipo':'Descripcion breve:',}
        widgets = {'nombre_tipo':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: Artistico.'}),
                   'descripcion_tipo': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Ejemplo: Este tipo de proyecto se aplica a diferentes campos de la Inteligenica Artificial.'}),}

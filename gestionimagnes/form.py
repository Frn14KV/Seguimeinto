#franklin
from django import forms
from gestionimagnes.models import Imagenes


class GuardarForm(forms.ModelForm):
    class Meta:
        model = Imagenes
        fields = "__all__"

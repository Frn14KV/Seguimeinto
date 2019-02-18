#franklin
from django import forms
from gestionarchivos.models import Archivos


class GuardarForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = "__all__"

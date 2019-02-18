#franklin
from django import forms
from gestionactas.models import Actas


class GuardarForm(forms.ModelForm):
    class Meta:
        model = Actas
        fields = "__all__"

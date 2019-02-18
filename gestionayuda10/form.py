#franklin
from django import forms
from gestionayuda10.models import Ayuda10


class GuardarForm10(forms.ModelForm):
    class Meta:
        model = Ayuda10
        fields = "__all__"

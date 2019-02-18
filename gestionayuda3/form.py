#franklin
from django import forms
from gestionayuda3.models import Ayuda3


class GuardarForm3(forms.ModelForm):
    class Meta:
        model = Ayuda3
        fields = "__all__"

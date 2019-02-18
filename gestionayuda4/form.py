#franklin
from django import forms
from gestionayuda4.models import Ayuda4


class GuardarForm4(forms.ModelForm):
    class Meta:
        model = Ayuda4
        fields = "__all__"

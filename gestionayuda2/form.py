#franklin
from django import forms
from gestionayuda2.models import Ayuda2


class GuardarForm2(forms.ModelForm):
    class Meta:
        model = Ayuda2
        fields = "__all__"

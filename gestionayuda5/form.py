#franklin
from django import forms
from gestionayuda5.models import Ayuda5


class GuardarForm5(forms.ModelForm):
    class Meta:
        model = Ayuda5
        fields = "__all__"

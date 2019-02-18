#franklin
from django import forms
from gestionayuda9.models import Ayuda9


class GuardarForm9(forms.ModelForm):
    class Meta:
        model = Ayuda9
        fields = "__all__"

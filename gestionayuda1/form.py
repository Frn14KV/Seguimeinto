#franklin
from django import forms
from gestionayuda1.models import Ayuda1


class GuardarForm1(forms.ModelForm):
    class Meta:
        model = Ayuda1
        fields = "__all__"

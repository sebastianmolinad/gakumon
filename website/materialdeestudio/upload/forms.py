from django import forms
from .models import Parcial, Talleres, Apuntes


class UploadForm(forms.ModelForm):
    class Meta:
        model = Parcial
        fields = ['titulo', 'sede', 'docente', 'semestre', 'materia', 'facultad', 'imagen']
from django import forms

from .models import Materia

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["nombre", "año_materia", "docente" ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "año_materia": forms.TextInput(attrs={"class": "form-control"}),
            "docente": forms.TextInput(attrs={"class": "form-control"}),
        }
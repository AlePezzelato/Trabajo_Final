from django import forms
from .models import Docente


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ["nombre", "apellido",  "materia", "año"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
            "materia": forms.TextInput(attrs={"class": "form-control"}),
        }
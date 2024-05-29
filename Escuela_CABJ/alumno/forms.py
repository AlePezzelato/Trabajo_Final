from django import forms

from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["nombre", "apellido", "fecha_de_nacimiento", "año_curso", "docente_id", "materia_id" ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_de_nacimiento": forms.TextInput(attrs={"class": "form-control"}),
            "año_curso": forms.TextInput(attrs={"class": "form-control"}),
            "docente_id": forms.TextInput(attrs={"class": "form-control"}),
            "materia_id": forms.TextInput(attrs={"class": "form-control"}),
        }
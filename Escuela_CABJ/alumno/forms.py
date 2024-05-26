from django import forms

from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["nombre", "apellido", "fecha_de_nacimiento", "año_curso", "docente_id", "materia_id", "año" ]
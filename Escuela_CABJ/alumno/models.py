from django.db import models
from docente.models import Docente
from materia.models import Materia


# modela para la app alumno

class Alummno(models.Model):
    nombre = models.CharField(max_length=250),
    apellido = models.CharField(max_length=150)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    año_curso= models.IntegerField(max_length=2)
    docente_id = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    materia_id = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

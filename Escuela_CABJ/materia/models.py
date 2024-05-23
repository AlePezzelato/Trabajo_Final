from django.db import models
from docente.models import Docente
from alumno.models import Alumno

# modelos para usar en la app materia

class Materia(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    codigo = models.CharField(max_length=30, unique=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True)
    alumnos = models.ManyToManyField(Alumno)
    
    def __str__(self) -> str:
        return self.nombre




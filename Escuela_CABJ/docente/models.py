from django.db import models
from materia.models import Materia
from alumno.models import Alumno


# Modelo para usar en la app docente

class Docente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    materia_id = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True, blank=True)
    año = models.PositiveBigIntegerField(unique=True)
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"



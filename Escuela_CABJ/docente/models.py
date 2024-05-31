from django.db import models
#from alumno.models import Año
from materia.models import Materia



# Modelo para usar en la app docente

class Docente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    materia = models.CharField(max_length=100, null=True, unique=False)
    año = models.IntegerField(null=True, unique=False)
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Curso(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True, blank=True)
    #año = models.ForeignKey(Año, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.docente}"
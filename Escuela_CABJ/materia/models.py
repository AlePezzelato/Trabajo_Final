from django.db import models


# modelos para usar en la app materia

class Materia(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    codigo = models.CharField(max_length=30, unique=True)
    docente = models.ForeignKey("docente.Docente", related_name="materias", on_delete=models.SET_NULL, null=True, blank=True)
    alumnos = models.ManyToManyField("alumno.Alumno", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nombre




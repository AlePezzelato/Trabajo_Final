from django.db import models


# modelos para usar en la app materia

class Materia(models.Model):
    nombre = models.CharField(max_length=150, unique=False)
    año_materia= models.IntegerField(null=True, unique=False)
    docente = models.CharField(max_length=150, null=True,  unique=False)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.año_materia} {self.docente}"




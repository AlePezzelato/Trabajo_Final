from django.db import models

# modelos para usar en la app materia

class Materia(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    codigo = models.CharField(max_length=30, unique=True)
    
    def __str__(self) -> str:
        return self.nombre


# Create your models here.

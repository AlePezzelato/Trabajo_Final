from django.db import models



# modela para la app alumno

class Alumno(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=150)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    año_curso= models.PositiveBigIntegerField(null=True)
    docente_id = models.ForeignKey("docente.Docente", on_delete=models.SET_NULL, null=True)
    materia_id = models.ForeignKey("materia.Materia", on_delete=models.SET_NULL, null=True)
    año = models.ManyToManyField("Año", through="Inscripcion")
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

class Año(models.Model):
    año = models.CharField(max_length=4)

    def __str__(self):
        return self.año

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    año = models.ForeignKey(Año, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alumno} en {self.año}"

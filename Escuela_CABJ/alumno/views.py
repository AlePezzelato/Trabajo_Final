from django.shortcuts import render

from . import models

#Vistas para la app alumno

def index(request):
    consulta = models.Alumno.objects.all()
    contexto = {"Alumno": consulta}
    return render (request, "alumno/index.html", contexto)

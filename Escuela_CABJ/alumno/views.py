from django.shortcuts import render, redirect

from . import models
from alumno.forms import AlumnoForm

#Vistas para la app alumno


def index(request):
    return render(request, "alumno/index.html")


def listado_alumnos(request):
    consulta = models.Alumno.objects.all()
    contexto = {"alumnos": consulta}
    return render (request, "alumno/listado_alumnos.html", contexto)

def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alumno:listado_alumnos")
    else:
        form = AlumnoForm()
    return render(request, "alumno/crear_alumno.html", {"form": form})
    

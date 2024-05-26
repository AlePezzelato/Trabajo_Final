from django.shortcuts import render
from . import models

def index(request):
    return render (request, "docente/index.html")

def listado_docentes(request):
    consulta = models.Docente.objects.all()
    contexto = {"docentes": consulta}
    return render (request, "docente/listado_docentes.html", contexto)


from django.shortcuts import render, redirect
from docente.models import Docente
from docente.forms import DocenteForm


def index(request):
    return render(request, "docente/index.html")


def listado_docentes(request):
    consulta = Docente.objects.all()
    contexto = {"docentes": consulta}
    return render (request, "docente/listado_docentes.html", contexto)

def crear_docente(request):
    if request.method == "POST":
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("docente:listado_docentes")
    else:
        form = DocenteForm()
    return render(request, "docente/crear_docente.html", {"form": form})


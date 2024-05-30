from django.shortcuts import render, redirect
from docente.models import Docente
from docente.forms import DocenteForm


def index(request):
    return render(request, "docente/index.html")


def listado_docentes(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Docente.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Docente.objects.all()
        contexto = {"docente": consulta}
    return render(request, "docente/listado_docentes.html", contexto)

def crear_docente(request):
    if request.method == "POST":
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("docente:listado_docentes")
    else:
        form = DocenteForm()
    return render(request, "docente/crear_docente.html", {"form": form})

def detalle_docentes(request, pk: int):
    consulta = Docente.objects.get(id=pk)
    contexto = {"docente": consulta}
    return render (request, "docente/detalle_docentes.html", contexto)

def actualizar_docente(request, pk: int):
    consulta = Docente.objects.get(id=pk)
    if request.method == "POST":
        form = DocenteForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("docente:listado_docentes")
    else:  # GET
        form = DocenteForm(instance=consulta)
    return render(request, "docente/crear_docente.html", {"form": form})

def borrar_docente(request, pk: int):
    consulta = Docente.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("docente:listado_docentes")
    return render(request, "docente/confirma_borrar.html", {"object": consulta})
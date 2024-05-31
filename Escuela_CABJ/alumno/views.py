from django.shortcuts import render, redirect

from alumno.models import Alumno
from alumno.forms import AlumnoForm

#Vistas para la app alumno


def index(request):
    return render(request, "alumno/index.html")


def listado_alumnos(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Alumno.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Alumno.objects.all()
    contexto = {"alumnos": consulta}
    return render(request, "alumno/listado_alumnos.html", contexto)


def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alumno:listado_alumnos")
    else:
        form = AlumnoForm()
    return render(request, "alumno/crear_alumno.html", {"form": form})
    
def actualizar_alumno(request, pk:int):
    consulta = Alumno.objects.get(id=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("alumno:listado_alumnos")
    else:
        form = AlumnoForm(instance=consulta)
    return render(request, "alumno/crear_alumno.html", {"form": form})

def detalle_alumno(request, pk:int):
    consulta = Alumno.objects.get(id=pk)
    contexto = {"alumno": consulta}
    return render(request, "alumno/detalle_alumnos.html", contexto)


def borrar_alumno(request, pk:int):
    consulta = Alumno.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("alumno:listado_alumnos")
    else:
        return render(request, "alumno/confirma_borrar_alumno.html", {"alumno":consulta})
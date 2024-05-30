from django.shortcuts import render, redirect
from materia.models import Materia
from materia.forms import MateriaForm

def index(request):
    return render (request, "materia/index.html")

def listado_materias(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Materia.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Materia.objects.all()
    contexto = {"materias": consulta}
    return render(request, "materia/listado_materias.html", contexto)

def crear_materia(request):
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("materia:listado_materias")
    else:
        form = MateriaForm()
    return render(request, "materia/crear_materia.html", {"form": form})
    
def actualizar_materia(request, pk:int):
    consulta = Materia.objects.get(id=pk)
    if request.method == "POST":
        form = MateriaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("materia:listado_materias")
    else:
        form = MateriaForm(instance=consulta)
    return render(request, "materia/crear_materia.html", {"form": form})   

def detalle_materia(request, pk:int):
    consulta = Materia.objects.get(id=pk)
    contexto = {"materia": consulta}
    return render(request, "materia/detalle_materias.html", contexto)

def borrar_materia(request, pk:int):
    consulta = Materia.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("materia:listado_materias")
    else:
        return render(request, "materia/confirma_borrar_materia.html", {"materia":consulta})
    



#def listado_materias(request):
#    consulta = Materia.objects.all()
#    contexto = {"materias": consulta}
#  return render (request, "materia/listado_materias.html", contexto)

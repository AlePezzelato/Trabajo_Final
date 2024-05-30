from django.urls import path

from docente.views import listado_docentes, index, crear_docente, detalle_docentes, actualizar_docente, borrar_docente
app_name = "docente"

urlpatterns = [
    path("", index, name="index"),
    path("listado_docentes", listado_docentes, name="listado_docentes"),
    path("crear_docente", crear_docente, name="crear_docente"),
    path("detalle_docente<int:pk>", detalle_docentes, name="detalle_docente"),
    path("actualizar_docente<int:pk>", actualizar_docente, name="actualizar_docente"),
    path("borrar_docente<int:pk>", borrar_docente, name="borrar_docente"),
]
    


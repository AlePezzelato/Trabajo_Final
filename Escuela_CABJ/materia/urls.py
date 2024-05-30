from django.urls import path

from materia.views import index, listado_materias, crear_materia,  borrar_materia, actualizar_materia, detalle_materia

app_name = "materia"

urlpatterns = [
    path("", index, name="index"),
    path("listado_materias", listado_materias, name="listado_materias"),
    path("crear_materia", crear_materia, name="crear_materia"),
    path("detalle_materia/<int:pk>", detalle_materia, name="detalle_materia"),
    path("actualizar_materia/<int:pk>", actualizar_materia, name="actualizar_materia"),
    path("borrar_materia/<int:pk>", borrar_materia, name="borrar_materia"),
]
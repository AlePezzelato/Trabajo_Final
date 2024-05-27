from django.urls import path

from alumno.views import listado_alumnos, index, crear_alumno, actualizar_alumno, borrar_alumno



app_name = "alumno"

urlpatterns = [
    path("", index, name="index"),
    path("listado_alumnos", listado_alumnos, name="listado_alumnos"),
    path("crear_alumno", crear_alumno, name="crear_alumno"),
    path("actualizar_alumno/<int:pk>", actualizar_alumno, name="actualizar_alumno"),
    path("borrar_alumno/<int:pk>", borrar_alumno, name="borrar_alumno"),
]
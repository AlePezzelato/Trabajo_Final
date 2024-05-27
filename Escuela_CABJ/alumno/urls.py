from django.urls import path

from alumno.views import listado_alumnos, index, crear_alumno

app_name = "alumno"

urlpatterns = [
    path("", index, name="index"),
    path("listado_alumnos", listado_alumnos, name="listado_alumnos"),
    path("crear_alumno", crear_alumno, name="crear_alumno")
]
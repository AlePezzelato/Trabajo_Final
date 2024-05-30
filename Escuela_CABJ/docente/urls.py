from django.urls import path

from docente.views import listado_docentes, index, crear_docente
app_name = "docente"

urlpatterns = [
    path("", index, name="index"),
    path("listado_docentes", listado_docentes, name="listado_docentes"),
    path("crear_docente", crear_docente, name="crear_docente"),
    ]


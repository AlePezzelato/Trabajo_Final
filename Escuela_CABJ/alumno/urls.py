from django.urls import path

from . import views

app_name = "alumno"

urlpatterns = [
    path("", views.index, name="index"),
]
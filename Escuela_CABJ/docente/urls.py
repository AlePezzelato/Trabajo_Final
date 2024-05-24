from django.urls import path

from . import views

app_name = "docente"

urlpatterns = [
    path("", views.index, name="index"),
]
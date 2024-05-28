from django.db import models
from django.contrib.auth.models import User

class Administracion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="administracion")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

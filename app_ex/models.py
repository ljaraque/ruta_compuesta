from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    descripcion = models.CharField(max_length=70)
    nacionalidad = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=4, decimal_places=1)
    peso = models.DecimalField(max_digits=4, decimal_places=1)
    direccion = models.CharField(max_length=300)
    codigo_postal = models.CharField(max_length=20)
    archivo_foto = models.CharField(max_length=400, default="sin asignar")
    rol = models.CharField(max_length=50, default="sin asignar")

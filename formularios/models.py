from django.db import models

# Create your models here.

class Guitarra(models.Model):
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=50)
    cuerdas = models.IntegerField()
    madera = models.CharField(max_length=20, default="No informada")
    fecha_compra = models.DateField()

class Musico(models.Model):
    nombre = models.CharField(max_length=80)
    guitarra = models.ForeignKey(Guitarra, on_delete=models.CASCADE)

from django.db import models

# Create your models here.

class Guitarra(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cuerdas = models.IntegerField()
    fecha_compra = models.DateField()

from django.db import models

# Create your models here.

class Musico(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=50, default="Vacante")
    pais = models.CharField(max_length=50, default="Chile")


class Guitarra(models.Model):
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=50)
    cuerdas = models.IntegerField()
    madera = models.CharField(max_length=20, default="No informada")
    fecha_compra = models.DateField()
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE, default=None)


class Banda(models.Model):
    nombre = models.CharField(max_length=80)
    fecha_formacion = models.DateField()
    musicos = models.ManyToManyField(Musico)


class Pasaporte(models.Model):
    codigo = models.CharField(max_length=50, unique=True, null=False)
    fecha_expiracion = models.DateField()
    musico = models.OneToOneField(Musico, on_delete=models.CASCADE)

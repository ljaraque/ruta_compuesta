import datetime

from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

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

    class Meta:
        ordering=['id']

class Banda(models.Model):
    nombre = models.CharField(max_length=80)
    fecha_formacion = models.DateField()
    musicos = models.ManyToManyField(Musico)


class Pasaporte(models.Model):
    codigo = models.CharField(max_length=50, unique=True, null=False)
    fecha_expiracion = models.DateField()
    musico = models.OneToOneField(Musico, on_delete=models.CASCADE)


# Modelos para Views Basadas en Clases

def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("2020-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo fechas de diciembre 2020")



class GuitarraCBV(models.Model):
    marca = models.CharField(
                max_length=80,
                validators=[validators.MinLengthValidator(
                                    4, 
                                    "Marca debe tener 4 caracteres mínimo!")]
                )
    modelo = models.CharField(
                max_length=50,
                validators=[validators.MinLengthValidator(2, 
                            "El modelo no puede ser de menos de 2 letras")]
                )
    cuerdas = models.IntegerField(
                validators=[validators.MaxValueValidator(10, "Número entre 6 y 10"),
                        validators.MinValueValidator(6,"Número entre 6 y 10"),]
                )
    madera = models.CharField(max_length=20, default="No informada")
    fecha_compra = models.DateField(validators=[validar_fecha])


    class Meta:
        ordering = ["id"]
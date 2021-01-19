from django.db import models

# Create your models here.


class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    pais = models.CharField(max_length=50, default="Chile")

class Guitarra(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cuerdas = models.IntegerField()
    madera = models.CharField(max_length=50, default="No informada")
    fecha_compra = models.DateField()
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.marca + self.modelo

    class Meta:
        ordering = ['-marca']

class Banda(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_formacion = models.DateField()
    musicos = models.ManyToManyField(Musico)


class Pasaporte(models.Model):
    codigo = models.CharField(max_length=50, unique=True, null=False)
    fecha_expiracion = models.DateField()
    musico = models.OneToOneField(Musico, on_delete=models.CASCADE)

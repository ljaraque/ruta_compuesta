import datetime
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import GuitarraCBV


def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("2020-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo fechas de diciembre 2020")


class PrimerFormulario(forms.Form):
    marca = forms.CharField(
                widget = forms.TextInput(
                                attrs = {'style': 'border-color: blue;'}),
                validators=[validators.MinLengthValidator(
                        4, 
                        "Marca debe tener 4 caracteres mínimo!")])
    modelo = forms.CharField(validators=[validators.MinLengthValidator(2, 
                            "El modelo no puede ser de menos de 2 letras")
                        	  ])
    cuerdas = forms.IntegerField(
                validators=[validators.MaxValueValidator(10, "Número entre 6 y 10"),
                        validators.MinValueValidator(6,"Número entre 6 y 10"),])
    fecha_compra = forms.DateField(
                validators=[validar_fecha]
    )


# Form for Vistas Basadas en Clases

class PrimerFormularioCBV(forms.ModelForm):
    class Meta:
        model = GuitarraCBV
        fields = '__all__'
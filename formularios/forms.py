from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
import datetime

def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("2020-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo fechas de diciembre 2020")

class PrimerFormulario(forms.Form):
    marca = forms.CharField(
                    widget=forms.TextInput(
                        attrs={'style': 'border-color: blue;'}),
                    validators=[
                        validators.MinLengthValidator(
                            4, 
                            "La marca no puede ser de menos de 4 letras"
                            )
                        ])
    modelo = forms.CharField(
                    validators=[
                        validators.MinLengthValidator(
                            2, 
                            "El modelo no puede ser de menos de 2 letras"
                            )
                        ], required=False)
    cuerdas = forms.IntegerField(initial=6,
            validators=[validators.MaxValueValidator(10, "Número entre 6 y 10"),
                        validators.MinValueValidator(6,"Número entre 6 y 10"),] 

    )
    fecha_compra = forms.DateField(
                    initial=datetime.datetime.now().strftime("%Y-%m-%d"),
                    validators=[validar_fecha])
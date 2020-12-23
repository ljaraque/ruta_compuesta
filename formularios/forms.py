from django import forms

class PrimerFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    cuerdas = forms.IntegerField()
    fecha_compra = forms.DateField()

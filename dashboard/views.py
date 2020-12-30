from django.http import HttpResponseRedirect
from django.shortcuts import render
import random

# Create your views here.

def grafico_principal(request):
    return render(
        request, 
        'dashboard/grafico.html',
    )


def grafico_charts(request):
    datos_aleatorios = list()
    etiquetas = list()
    for i in range(0,15):
        datos_aleatorios.append(random.randint(2, 50))
        etiquetas.append("Dato_"+str(i+1))
    context = {'datos_grafico1':[10,15,18,20, 50, 70],
                'etiquetas_grafico1':["Dato1", "Dato2", "Dato3", "Dato4", "Dato5", "Dato6"],
                'datos_grafico2':datos_aleatorios,
                'etiquetas_grafico2':etiquetas}
    return render(request, 'dashboard/grafico_charts.html', context)

def google(request):
    return HttpResponseRedirect('https://www.google.com')
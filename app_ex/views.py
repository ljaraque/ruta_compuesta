from django.shortcuts import render
from django.conf import settings
import csv

# Create your views here.

def inicio(request):
    return render(
        request, 
        'app_ex/elefante.html', 
        context={'texto':'Texto de Ejercicio 1'}
        )

def empresa(request):
    return render(
        request, 
        'app_ex/empresa.html', 
        context={'texto':'Texto de Ejercicio 1'}
        )

def contacto(request):
    return render(
        request, 
        'app_ex/contacto.html', 
        context={'texto': 'Texto de Ejercicio 1'}
        )

import random 

def personas(request): 
    nombres = ['Juana', 'Rosa', 'Luis', 'Rodrigo','Sarah', 'Rocio', 'Emmanuel'] 
    nuevos = ['Lucía', 'Ronaldo'] 
    lista_aleatoria = [i for i in range(random.randint(1,10))] 
    datos = {'nombres' : nombres, 'otros' : nuevos, 'año' : '2020', 'lista' : lista_aleatoria} 
    return render(request, 'app_ex/personas.html', context=datos)

def tabladatos(request):
    filename= "/app_ex/static/app_ex/data/iris.csv"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        data = csv.DictReader(file)
        data_list = []
        for fila in data:
            data_list.append(fila)

        context = {'texto': 'Estos son datos de iris',
                    'data': data_list}
    return render(request, 'app_ex/iris.html', context = context)

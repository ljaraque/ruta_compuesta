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
        context={'texto':'Texto de Ejercicio 1'}
        )

def personas(request) :
    nombres = ['Juana', 'Rosa', 'Luis', 'Rodrigo']
    nuevos = ['Lucía', 'Ronaldo']
    print(str(settings.BASE_DIR))
    filename= "/app_ex/static/app_ex/data/iris.csv"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        data = csv.DictReader(file)
        data_list = list()
        for row in data:
            data_list.append(row)
        #print(data_list)
    context = {'nombres' : nombres, 
                'otros' : nuevos, 
                'año' : '2020', 
                'lista':[3,4,4,5,6],
                'data': data_list }
    return render(request, 'app_ex/personas.html', context)
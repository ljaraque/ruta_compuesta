from django.shortcuts import render

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

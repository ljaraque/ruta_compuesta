import json

from django.shortcuts import render, redirect
from .forms import PrimerFormulario
from django.conf import settings
from .models import Guitarra


def crear_guitarra(request):
    form = PrimerFormulario()
    context = {'formulario': form}
    return render(request, 'formularios/index.html', context = context)

def crear_guitarra2(request):
    template = 'formularios/index_manual.html'
    form = PrimerFormulario(request.POST or None)    
    if form.is_valid():
        print("datos recibidos!\n", dir(form))
        form_data = form.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        print(form.data)
        filename= "/formularios/static/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            guitarras=json.load(file)
        guitarras['guitarras'].append(form_data)
        print(form.data)
        with open(str(settings.BASE_DIR)+filename, "w") as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    return render(request, template, 
                    {"formulario": form})

def crear_exitoso(request):
    filename= "/formularios/static/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        guitarras=json.load(file)
    return render(request, 'formularios/crear_exitoso.html', context=guitarras)


def prueba_models(request):
    for i in range(0,4):
        guitarra = Guitarra(marca='Jackson', modelo='RR3', cuerdas=7, fecha_compra='2020-12-01')
        guitarra.save()
    
    valores = { 'guitarras': Guitarra.objects.all(),
                'guitarras_values': Guitarra.objects.values()}
    print(valores)
    return render(request, 'formularios/prueba_models.html', context=valores)
    
    
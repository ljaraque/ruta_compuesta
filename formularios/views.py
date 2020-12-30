from django.shortcuts import render, redirect
from .forms import PrimerFormulario
from django.conf import settings
import json

# Create your views here.
def crear_guitarra(request):
    formulario = PrimerFormulario(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        filename= "/formularios/static/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            guitarras=json.load(file)
        guitarras['guitarras'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    return render(request, 'formularios/crear_guitarra.html', context)


def crear_guitarra_manual(request):
    formulario = PrimerFormulario(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        filename= "/formularios/static/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            guitarras=json.load(file)
        guitarras['guitarras'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    return render(request, 'formularios/crear_guitarra_manual.html', context)

def crear_exitoso(request):
    filename= "/formularios/static/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        guitarras=json.load(file)
    return render(request, 'formularios/crear_exitoso.html', context=guitarras)
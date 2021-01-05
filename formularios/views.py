from django.shortcuts import render, redirect
from .forms import PrimerFormulario
from django.conf import settings
import json

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
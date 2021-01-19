from django.shortcuts import render, redirect
from .forms import PrimerFormulario
from django.conf import settings
import json
from .models import Guitarra, Musico, GuitarraCBV
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.contrib import messages


#CRUD: CREATE con archivo
def crear_guitarra(request):
    formulario = PrimerFormulario(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        filename= "/formularios/static/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            guitarras=json.load(file)
        form_data['id'] = guitarras['ultimo_id_generado'] + 1
        guitarras['ultimo_id_generado'] = form_data['id']
        guitarras['guitarras'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    return render(request, 'formularios/crear_guitarra.html', context)


#CRUD: CREATE con Base de Datos
def crear_guitarra_db(request):
    formulario = PrimerFormulario(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        musico_primero = Musico.objects.all()[0]
        guitarra = Guitarra.objects.create(
                    marca=form_data['marca'], 
					modelo=form_data['modelo'], 
					cuerdas=form_data['cuerdas'], 
					fecha_compra=form_data['fecha_compra'],
                    musico = musico_primero
                    )
        messages.success(request, 'La guitarra de ID= '+str(guitarra.id)+' ha sido creada!, Felicitaciones')
        return redirect('formularios:lista_guitarras_db')
    return render(request, 'formularios/crear_guitarra_db.html', context)


'''
def crear_guitarra_manual(request):
    formulario =Guitarra.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        filename= "/formularios/static/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            guitarras=json.load(file)
        form_data['id'] = guitarras['ultimo_id_generado'] + 1
        guitarras['ultimo_id_generado'] = form_data['id']
        guitarras['guitarras'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    return render(request, 'formularios/crear_guitarra_manual.html', context)
'''



#CRUD: READ con archivo JSON
def crear_exitoso(request):
    filename= "/formularios/static/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        guitarras=json.load(file)
    return render(request, 'formularios/crear_exitoso.html', context=guitarras)


#CRUD: READ con Base de Datos
def lista_guitarras_db(request):
    lista_guitarras = list(Guitarra.objects.all().values())
    guitarras = {'guitarras': lista_guitarras}
    return render(request, 'formularios/lista_guitarras_db.html', context=guitarras)


class ListaGuitarrasView(View):
    template_name = 'formularios/lista_guitarras_db.html'
    model = Guitarra

    def get(self, request):
        lista_guitarras = list(self.model.objects.all().values())
        guitarras = {'guitarras': lista_guitarras}
        return render(request, self.template_name , context=guitarras)

#CRUD: UPDATE CON BASE DE DATOS
def editar_guitarra_db(request, id):
    guitarra = Guitarra.objects.filter(id=id).values()[0]
    formulario = PrimerFormulario(request.POST or None, initial=guitarra)    
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        musico = guitarra['musico_id']
        Guitarra.objects.filter(id=id).update(
                    marca=form_data['marca'], 
					modelo=form_data['modelo'], 
					cuerdas=form_data['cuerdas'], 
					fecha_compra=form_data['fecha_compra'],
                    musico = musico
                    )

        return redirect('formularios:lista_guitarras_db')
    context = {'form': formulario, 'id' : id}
    return render(request, 'formularios/editar_guitarra_db.html', context)


#CRUD: UPDATE CON BASE DE DATOS Y CLASE VIEW
class EditarGuitarraView(View):
    template_name =  'formularios/editar_guitarra_db.html'
    model = Guitarra

    def get(self, id):
        guitarra = self.model.objects.filter(id=id).values()[0]
        formulario = PrimerFormulario(request.POST or None, initial=guitarra)
        context = {'form': formulario, 'id' : id}
        return render(request, self.template_name , context)

    def post(self):
        if formulario.is_valid():
            form_data = formulario.cleaned_data
            form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
            musico = guitarra['musico_id']
            self.model.objects.filter(id=id).update(
                        marca=form_data['marca'], 
                        modelo=form_data['modelo'], 
                        cuerdas=form_data['cuerdas'], 
                        fecha_compra=form_data['fecha_compra'],
                        musico = musico
                        )

            return redirect('formularios:lista_guitarras_db')


# Esta clase EditarGuitarraNada hereda de EditarGuitarraView que hemos creado arria, 
# e intenta ilustrar la forma en que llegan a ser posibles las clases:
# CrearGuitarra, EditarGuitarra, ListaGuitarras, EliminarGuitarra 
# solo definiendo 1 a 3 lineas de atributos solamente. 
# path() en urls.py no ha sido implementada para esta vista.
class EditarGuitarraNada(EditarGuitarraView):
    template_name = 'formularios/editar_guitarra_nada.html'
    model = Guitarra


#CRUD: DELETE con archivo JSON
def eliminar_guitarra(request, id):
    if request.method == "POST":
        filename= "/formularios/static/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            guitarras=json.load(file)
        for guitarra in guitarras['guitarras']:
            print(int(guitarra['id']), int(id))
            if int(guitarra['id']) == int(id):
                guitarras['guitarras'].remove(guitarra)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    context = {'id': id} 
    return render(request, "formularios/eliminar_guitarra.html", context)


#CRUD: DELETE con Base de Datos
def eliminar_guitarra_db(request, id):
    if request.method == "POST":
        Guitarra.objects.filter(id=id).delete()
        return redirect('formularios:lista_guitarras_db')
    context = {'id': id} 
    return render(request, "formularios/eliminar_guitarra_db.html", context)



def grafico2(request):
    lista = []
    filename= "/formularios/static/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        guitarras=json.load(file)
        diccionario = guitarras.get('guitarras')
        for elemento in diccionario[-5:]:
            cuerdas = elemento.get('cuerdas')
            lista.append(cuerdas)
    context = {'valor' : lista}
    return render(request, "formularios/grafico2.html", context)

def prueba_models(request):
    for i in range(0,1):
        guitarra = Guitarra(marca='Jackson', 
					modelo='RR3', 
					cuerdas=7, 
					fecha_compra='2020-12-01')
        guitarra.save()
    guitarras = Guitarra.objects.values()
    context = {'guitarras': guitarras}
    return render(request, 'formularios/prueba_models.html', context)

#CRUD vistas basadas en clases

'''
# esta clase se dejó comentada pues la alteramos para mostrar que también 
# se puede personalizar a cierto nivel
class ListGuitarras(ListView):
    model=GuitarraCBV
'''

# Clase ListView utilizada sobreescribiendo los atributos por defecto
# para model, template_name, context_object_name, extra_context
class ListaGuitarras(ListView):
    model=GuitarraCBV
    template_name = "formularios/template_nombre_manual.html"
    context_object_name = "guitarras"
    extra_context = {'fecha_hoy': "18 de Enero 2021", 'saludo': "Hola amigos!!"}


class CrearGuitarra(CreateView):
    model=GuitarraCBV
    fields='__all__'
    success_url=reverse_lazy('formularios:lista_guitarras_db_cbv')


class EliminarGuitarra(DeleteView):
    model=GuitarraCBV
    fields='__all__'
    success_url=reverse_lazy('formularios:lista_guitarras_db_cbv')


class EditarGuitarra(UpdateView):
    model=GuitarraCBV
    fields='__all__'
    success_url=reverse_lazy('formularios:lista_guitarras_db_cbv')



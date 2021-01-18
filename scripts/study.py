# Este es un script de aprendizaje

import inspect

from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from formularios.views import *

def analiza_vista(clase_vista):
    print("==================================================================")
    print("NOMBRE:\n", str(clase_vista))
    print("------------------------------------------------------------------")
    print("CONTENIDO:\n", dir(clase_vista))
    print("------------------------------------------------------------------")
    print("HERENCIA:\n", clase_vista.__mro__)
    print()


def inspecciona_instancia(objeto):
    print("\n\n\n\n\n==========================================================")
    print("\nInspeccionando Instancia {}!".format(str(objeto)))
    print("------------------------------------------------------------")
    print("\ndir:\n", dir(objeto))
    for k, v in objeto.__dict__.items():
        print("------------------------------------------------------------")
        if not callable(v):
            print(k, ": ",v)
        else:
            print(k, ":\n", inspect.getsource(v))
    print("\nFin de la Inspección!")
    print("\n==============================================================")
    print({k: getattr(objeto, k) for k in dir(objeto)})


def inspecciona_clase(objeto):
    for i in range(0,25):
        print("==============================================================")
    print("\nInspeccionando Clase {}!".format(str(objeto)))
    print("------------------------------------------------------------")
    print("\ndir:\n", dir(objeto))
    print("--------------------------------------------
    print("NOMBRE:\n", str(clase_vista))
    print("------------------------------------------------------------------")
    print("CONTENIDOn dir(objeto)}
    for k, v in diccionario_objeto.items():
        print("------------------------------------------------------------")
        if not callable(v):
            print(k, ": ",v)
        else:
            try:
                print(k, ":\n", inspect.getsource(v))
            except Exception as e:
                print(k, ":\n", "NO DISPONIBLE!!")
    print("\nFin de la Inspección!")
    print("\n==============================================================")


def muestra_atributos_publicos(objeto):
    return [k for k, v in vars(objeto).items() if
            not (k.startswith('_'))]

def run():
    analiza_vista(View)
    analiza_vista(TemplateView)
    analiza_vista(RedirectView)
    analiza_vista(DetailView)
    analiza_vista(ListView)
    analiza_vista(CreateView)
    analiza_vista(UpdateView)
    analiza_vista(DeleteView)

    analiza_vista(EditarGuitarraView)
    print(EditarGuitarraView.template_name)

    inspecciona_instancia(EditarGuitarraView)

    inspecciona_instancia(EditarGuitarra)

    inspecciona_clase(EditarGuitarraView)
    inspecciona_clase(EditarGuitarra)


    
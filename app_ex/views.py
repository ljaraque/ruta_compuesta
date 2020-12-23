from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.conf import settings
import csv
# these two following lines avoid back button to see previous page
# after user is logged out
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required


# Create your views here.

# these two following lines avoid back button to see previous page
# after user is logged out
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def inicio(request):
    if request.user.is_authenticated:
        for key in request.session.keys():
            print(key + " :=>" + request.session[key])
        return render(
                    request, 
                    'app_ex/elefante.html', 
                    context={'texto':'Texto de Ejercicio 1'}
                    )
    loginurl = reverse('login') + '?' + urlencode({'next': request.path})
    return redirect(loginurl)


# TRES OPCIONES PARA empresa/, CBV con TemplateView, con View y FBV
from django.contrib.auth.mixins import LoginRequiredMixin
# OJO: Como CBV es automatica, si no está autenticado direccionará a default
# "accounts/login", esto se cambia en settings.py con LOGIN_URL = '/cuentas/login'
## IMPORTANTE: cache_control y login_required no funcionan en CBV
## debe revisarse cómo lograr evitar back button con CBV
class EmpresaView(LoginRequiredMixin, TemplateView):
    template_name = "app_ex/empresa.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = reverse('login')+'?'+urlencode({'next': self.request.path})
        return context


'''
#en este caso no se puede usar template_name pues View no posee ese atributo
class EmpresaView(LoginRequiredMixin, View):

    def get(self, request):
        return render(
            request, 
            'app_ex/empresa.html', 
            context = {'texto':'Texto de Ejercicio 1', 'next':reverse('login')+'?'+urlencode({'next': request.path})}
            )
'''

# FBV empresa
'''
def empresa(request):
    return render(
        request, 
        'app_ex/empresa.html', 
        context={'texto':'Texto de Ejercicio 1'}
        )
'''

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
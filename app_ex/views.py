from django.shortcuts import render
from django.conf import settings
import csv
import uuid
from django.views.generic.base import View

# Create your views here.

def inicio(request):
    print("Cookies", request.COOKIES)
    response = render(
        request, 
        'app_ex/elefante.html', 
        context={'texto':'Texto de Ejercicio 1'}
        )

    if 'Identificador' not in request.COOKIES:
        response.set_cookie(
                    key = 'Identificador',
                    value = uuid.uuid4(),
                    max_age = 60*60*24*30 #seg*min*dias*mes
        )

    response.set_cookie(
                key = 'V.I.P',
                value = "Eres un ganador"
        )
    return response

#Forma facil de hacer login con django
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
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
from django.shortcuts import reverse, redirect
from django.utils.http import urlencode

#VALIDANDO QUE EL USUARIO SE ENCUENTRE AUTENTICADO SI NO ESTA AUTENTICADO TE ENVIA AL LOGIN CON UN NEXT

def personas(request):
    if not request.user.is_authenticated :
        loginurl = reverse('login')+'?'+urlencode({'next': request.path})
        print(loginurl)
        return redirect(loginurl)
 
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

        datos_para_context = {'texto': 'Estos son datos de iris',
                    'data': data_list}

    if 'visitas' not in request.session:
        request.session['visitas']= 1
    else:
        if request.session['visitas']<10:
            request.session['visitas'] += 1
        else:
            request.session['visitas'] = 1
    datos_para_context['num_visitas']=request.session['visitas']

    return render(request, 'app_ex/iris.html', context = datos_para_context)

def map(request):
    return render(request,'app_ex/map.html')


from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class MiPerfil(LoginRequiredMixin, View):
    def get(self, request):
        usuario_id = request.user.id #OBTENER ID DEL USUARIO QUE ESTA VISITANDO LA VISTA
        perfil = Profile.objects.filter(usuario_id=usuario_id).values()[0]
        print(perfil)
        context = {'perfil':perfil}
        return render(request, 'app_ex/pagina_personalizada.html', context=context)


from django.contrib.auth.mixins import UserPassesTestMixin


def es_jefe(user):
    rol = user.profile.rol
    if rol == "Jefe":
        return True
    else:
        return False 
    

class ListaEmpleados(LoginRequiredMixin, UserPassesTestMixin, View):
    
    def test_func(self):
        user = self.request.user
        return es_jefe(user)

    def get(self, request):
        usuario_id = request.user.id
        perfiles = Profile.objects.filter()
        context = {'perfiles': perfiles}
        return render(request, 'app_ex/lista_empleados.html', context)



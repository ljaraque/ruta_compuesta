from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def grafico_principal(request):
    return render(
        request, 
        'dashboard/grafico.html', context={'img_base_url': reverse('dashboard:grafico')}
    )

def google(request):
    return HttpResponseRedirect('https://www.google.com')
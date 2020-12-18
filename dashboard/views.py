from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def grafico_principal(request):
    return render(
        request, 
        'dashboard/grafico.html',
    )

def google(request):
    return HttpResponseRedirect('https://www.google.com')
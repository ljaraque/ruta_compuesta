
from django.urls import path
from . import views

app_name = "app_ex"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("empresa/", views.EmpresaView.as_view()),
    #path("empresa/", views.empresa),
    path("contacto/", views.contacto),
    path("personas/", views.personas),    
]
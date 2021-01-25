
from django.urls import path
from . import views

app_name = "app_ex"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("empresa/", views.empresa, name="empresa"),
    path("contacto/", views.contacto, name="contact"),
    path("personas/", views.personas, name="personas"),
    path("tabladatos/", views.tabladatos, name="tabladatos"),
    path("map/", views.map, name="map"),
    path("mi_perfil/", views.MiPerfil.as_view(), name="mi_perfil"),
    path("empleados", views.ListaEmpleados.as_view(), name="empleados")
]
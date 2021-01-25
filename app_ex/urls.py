
from django.urls import path
from . import views

app_name = "app_ex"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("empresa/", views.empresa, name="empresa"),
    path("contacto/", views.contacto, name="contacto"),
    path("personas/", views.personas, name="personas"),
    path("map/", views.map, name="map"),
    path("tabladatos/", views.tabladatos, name="tabladatos"),
    path("mi_perfil/", views.MiPerfil.as_view(), name="mi_perfil"),

]

from django.urls import path
from . import views

#app_name = "app_ex"

urlpatterns = [
    path("", views.inicio),
    path("empresa/", views.empresa),
    path("contacto/", views.contacto),
]
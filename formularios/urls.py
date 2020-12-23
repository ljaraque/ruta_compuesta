
from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('crear_guitarra', views.crear_guitarra),
]
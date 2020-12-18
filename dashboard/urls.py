
from django.urls import path
from . import views

#app_name = "dashboard"

urlpatterns = [
    path("grafico", views.grafico_principal),
    path("buscador", views.google)
]
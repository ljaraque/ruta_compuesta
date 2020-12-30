
from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("grafico", views.grafico_principal),
    path("grafico_charts", views.grafico_charts, name="grafico_charts"),
    path("buscador", views.google)
]
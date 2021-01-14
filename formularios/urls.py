
from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('crear_guitarra', views.crear_guitarra, name="crear_guitarra"),
    path('crear_exitoso', views.crear_exitoso, name="crear_exitoso"),
    path('<id>/borrar', views.eliminar_guitarra, name="eliminar_guitarra"),
    path('grafico2/', views.grafico2),
    path('prueba_models/', views.prueba_models, name="prueba_models"),
    path('crear_guitarra_db', views.crear_guitarra_db, name="crear_guitarra_db"),
    path('lista_guitarras_db', views.lista_guitarras_db, name="lista_guitarras_db"),
    path('<id>/borrar_db', views.eliminar_guitarra_db, name="eliminar_guitarra_db"),
]
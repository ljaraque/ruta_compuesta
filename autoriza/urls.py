from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "autoriza"

urlpatterns = [
    path('', TemplateView.as_view(template_name='autoriza/main.html')),
    path('productos', views.ProductosView.as_view(), name='productos'),
    path('python', views.DumpPython.as_view(), name='python'),
    path('inicio', views.InicioView.as_view(), name='inicio'),
    path('empresa', views.EmpresaView.as_view(), name='empresa'),
    path('equipo', views.EquipoView.as_view(), name='equipo'),
]

'''


'''
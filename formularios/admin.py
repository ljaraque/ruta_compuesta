from django.contrib import admin
from .models import Guitarra

# Register your models here.

@admin.register(Guitarra)
class GuitarraAdmin(admin.ModelAdmin):

    def get_musico(self, obj):
        nombre = obj.musico.nombre
        apellido = obj.musico.apellido
        return "{} {}".format(str(nombre), str(apellido))
    get_musico.short_description = 'nombre_musico'

    list_display = ('id', 'marca', 'modelo', 'cuerdas', 'madera', 'fecha_compra', 'get_musico')
    search_fields = ('marca', 'modelo', 'cuerdas', 'madera', 'fecha_compra', 'musico__nombre')


#admin.site.register(Guitarra)
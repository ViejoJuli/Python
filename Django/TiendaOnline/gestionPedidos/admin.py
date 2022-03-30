from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.
class ClientesAdmin(admin.ModelAdmin): #Permite ubicar otras columnas en el admin
    list_display=("nombre","direccion","tel")
    search_fields=("nombre","tel")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",) #Es una tupla, crear los filtros

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin) #Tener diponible la tabla de clientes
admin.site.register(Clientes,ClientesAdmin)

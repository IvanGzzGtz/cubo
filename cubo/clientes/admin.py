from django.contrib import admin
from .models import Clientes
# Register your models here.



class ClientesAdmin(admin.ModelAdmin):
    list_display = ['nombre_empresa', 'giro', 'telefono', 
                    'correo_electronico','tipo_cliente','tipo_mercancia','cantidad_de_viajes',
                    'northbound', 'southbound', 
                    'ctpat', 'nombre_contacto', 'telefono_contacto', 'correo_contacto',
                    'tax_id','calle', 'numero', 'colonia', 'ciudad', 
                     'codigo_postal', 'pais',]
    list_filter = ['tipo_cliente', 'tipo_mercancia']
    list_per_page = 20

admin.site.register(Clientes, ClientesAdmin)

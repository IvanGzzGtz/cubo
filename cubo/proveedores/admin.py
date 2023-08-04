from django.contrib import admin
from .models import Proveedores
# Register your models here.



class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre_empresa', 'giro', 'telefono', 'correo_electronico','tipo_proveedor','ctpat', 'nombre_contacto', 'telefono_contacto', 'correo_contacto','tax_id',
                     'calle', 'numero', 'colonia', 'ciudad', 
                     'codigo_postal', 'pais',]
    list_filter = ['tipo_proveedor']
    list_per_page = 20

admin.site.register(Proveedores, ProveedorAdmin)

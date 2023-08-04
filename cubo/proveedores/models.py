from django.db import models





class Proveedores(models.Model):

    tipo_proveedor = (
        ('Freight broker', 'Freight broker'),
        ('Owner operator', 'Owner operator'),
        ('Warehousing', 'Warehousing'),
        ('US Custom broker', 'US Custom broker'),
        ('Agente aduanal', 'Agente aduanal'),
        ('Lineas de transporte', 'Lineas de transporte'),

    )
    nombre_empresa = models.CharField(max_length=20)
    giro = models.CharField(max_length=100,  blank=True)
    telefono = models.IntegerField( blank=True, null=True)
    correo_electronico = models.CharField(max_length=100, blank=True)
    tipo_proveedor = models.CharField(max_length=30, choices=tipo_proveedor)
    cantidad_de_camiones = models.CharField(max_length=100,  blank=True)    
    tamano_de_cajas = models.CharField(max_length=100,  blank=True)    
    tipo_de_transporte = models.CharField(max_length=100,  blank=True)    # #Ejemplo de tipo de transportes de carga pesada, de caja chica, etc....
    ctpat = models.BooleanField(default=False)

    nombre_contacto = models.CharField(max_length=100,  blank=True)
    telefono_contacto = models.CharField(max_length=100,  blank=True)
    correo_contacto = models.CharField(max_length=100,  blank=True)

    tax_id = models.CharField(max_length=100,  blank=True)
    calle = models.CharField(max_length=100,  blank=True)
    numero = models.CharField(max_length=100,  blank=True)
    colonia = models.CharField(max_length=100,  blank=True)
    ciudad = models.CharField(max_length=100,  blank=True)
    codigo_postal = models.CharField(max_length=100,  blank=True)
    pais = models.CharField(max_length=100,  blank=True) 
    
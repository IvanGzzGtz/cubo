from django.db import models





class Clientes(models.Model):

    tipo_cliente = (
        ('Freight broker', 'Freight broker'),
        ('Owner operator', 'Owner operator'),
        ('Warehousing', 'Warehousing'),
        ('US Custom broker', 'US Custom broker'),
        ('Agente aduanal', 'Agente aduanal'),
        ('Lineas de transporte', 'Lineas de transporte'),

    )
    tipo_mercancia = (
        ('Perecedero', 'Perecedero'),
        ('Industrial', 'Industrial'),
    )

    nombre_empresa = models.CharField(max_length=20)
    giro = models.CharField(max_length=100,  blank=True)
    telefono = models.IntegerField( blank=True, null=True)
    correo_electronico = models.CharField(max_length=100, blank=True)
    tipo_cliente = models.CharField(max_length=30, choices=tipo_cliente)
    tipo_mercancia = models.CharField(max_length=30, choices=tipo_mercancia)
    cantidad_de_viajes = models.CharField(max_length=30)
    northbound = models.BooleanField(default=False)
    southbound = models.BooleanField(default=False)
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
    
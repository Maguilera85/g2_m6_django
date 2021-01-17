'''from django.db import models

# Create your models here.


class SensoresTemp(models.Model):
     tabla para sensores de temperatura

    nombre_sensor = models.CharField(max_length=20)
    temperatura = models.DecimalField(max_digits=2, decimal_places=1, default=None)
    fecha = models.DateField()

class SensoresApertura(models.Model):
     tabla para sensores de apertura 

    nombre_sensor = models.CharField(max_length=20)
    apertura = models.BooleanField()
    fecha = models.DateField()

class SensoresGas(models.Model):
     tabla para sensores de gasolina 

    nombre_sensor = models.CharField(max_length=20)
    gas_tipo = models.CharField(max_length=10, default=None)
    fecha = models.DateField() 

class CodigosAcceso(models.Model):
     Códigos numéricos ingresados por un usuario que intenta abrir una puerta de acceso 

    pin = models.IntegerField()'''

from django.db import models

class Persona(models.Model):

    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    dni = models.IntegerField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return self.dni
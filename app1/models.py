from django.db import models

# Create your models here.


class SensoresTemp(models.Model):
    ''' tabla para sensores de temperatura'''

    nombre_sensor = models.CharField(max_length=20)
    fecha = models.DateField()

class SensoresApertura(models.Model):
    ''' tabla para sensores de apertura '''

    nombre_sensor = models.CharField(max_length=20)
    fecha = models.DateField()

class SensoresGas(models.Model):
    ''' tabla para sensores de gasolina '''

    nombre_sensor = models.CharField(max_length=20)
    fecha = models.DateField() 

class CodigosAcceso(models.Model):
    ''' Códigos numéricos ingresados por un usuario que intenta abrir una puerta de acceso '''

    pin = models.IntegerField()
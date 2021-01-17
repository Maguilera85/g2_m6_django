from django.db import models

# Create your models here.


class Sensores(models.Model):
    temperatura = models.CharField(max_length=50)
    humedad= models.CharField(max_length=50)
    luz= models.CharField(max_length=50)
    color= models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    magnetico = models.CharField(max_length=50)
    velocidad = models.CharField(max_length=50)
    
class AperturaPuerta(models.Model):
    proximidad = models.CharField(max_length=50)
    opticos = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)

class NivelGasolina(models.Model):
    Ultrasónicos = models.CharField(max_length=10)
    Capacitivo = models.CharField(max_length=10)
    Flotador = models.CharField(max_length=50)

class CodigosNumericos(models.Model):
    nombre = models.CharField(max_length=50)
    
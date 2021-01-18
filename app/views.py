from django.shortcuts import render
from .models import AperturaPuerta, Sensores, NivelGasolina, CodigosNumericos



# Create your views here.
def sensores_tempe(request):
    for i in range(0,1):
        temperaturas = Sensores(temperatura='1.23 mm',
                                humedad='0.96 mm',
                                luz='1,44 N',
                                color='4.62 J',
                                posicion='4.64mm',
                                magnetico='2.72 HT',
                                velocidad='1.96 V')
        temperaturas.save()
    
    for i in range(0,1):
        apertura = AperturaPuerta(proximidad='2.99 mm',
                                opticos='9.18 mm',
                                contacto='1,78 N')
        apertura.save()
    
    for i in range(0,1):
        Nivel = NivelGasolina(Ultrasónicos='alto',
                                Capacitivo='alto',
                                Flotador='bajo')
        Nivel.save()
    
    for i in range(0,1):
        Codigo = CodigosNumericos( nombre='magnetico',
                                   fecha = 'fecha',
                                   observacion = ' temperatura  '
                                  )
        Codigo.save()
    
    temperaturas = Sensores.objects.values()
    apertura = AperturaPuerta.objects.values()
    Nivel = NivelGasolina.objects.values()
    Codigo = CodigosNumericos.objects.values()


    valores = { 'sensores1': temperaturas,
                'apertura1': apertura,
                'codigo': Codigo,
                'Nivel': Nivel}
                
    return render(request, 'app/sensores.html', valores)
    

    

from django.shortcuts import render
from .models import AperturaPuerta, Sensores, NivelGasolina, CodigosNumericos



# Create your views here.
def sensores_tempe(request):
    for i in range(0,1):
        temperaturas = Sensores(temperatura='0.83 mm',
                                humedad='9.16 mm',
                                luz='4,64 N',
                                color='6.72 J',
                                posicion='2.44mm',
                                magnetico='1.52 HT',
                                velocidad='9.66 V')
        temperaturas.save()
    
    for i in range(0,1):
        apertura = AperturaPuerta(proximidad='3.19 mm',
                                opticos='8.98 mm',
                                contacto='1,78 N')
        apertura.save()
    
    for i in range(0,1):
        Nivel = NivelGasolina(Ultrasónicos='medio',
                                Capacitivo='bajo',
                                Flotador='bajo')
        Nivel.save()
    
    for i in range(0,1):
        Codigo = CodigosNumericos( nombre='contacto',
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
    

    

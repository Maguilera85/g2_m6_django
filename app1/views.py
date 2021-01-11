from django.shortcuts import render
from .models import SensoresApertura, SensoresGas, SensoresTemp, CodigosAcceso
# Create your views here.





def mostrar_tablas(request):
    return render(request, 'app1/mostrar_tablas.html')

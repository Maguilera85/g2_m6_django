'''from django.shortcuts import render
from .models import SensoresApertura, SensoresGas, SensoresTemp, CodigosAcceso
# Create your views here.





def mostrar_tablas(request):
    data ={ 
        'form': Mostrar_tablasFrom()
    }
    return render(request, 'app1/mostrar_tablas.html')


def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario'''

from django.views.generic import ListView

from .models import Persona

class PersonaList(ListView):

    model = Persona
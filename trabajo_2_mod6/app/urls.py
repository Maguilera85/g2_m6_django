from django.urls import path
from . import views

urlpatterns = [
    path('', views.sensores_tempe, name='temperatura'),
    
    
]

'''path('', views.nivelgasolina, name='nombres'),
    path('', views.codigonumerico, name='nombres'),'''
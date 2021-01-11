from . import views
from django.urls import path

app_name = 'app1'

urlpatterns = [
    path("mostrar_tablas/", views.mostrar_tablas, name='mostrar_tablas'),
]
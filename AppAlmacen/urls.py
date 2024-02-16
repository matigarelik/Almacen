# AppAlmacen/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('clientes/', views.clientes, name='clientes'),
    path('buscar/', views.buscar, name='buscar'),
    # Agrega aquí más patrones de URL según sea necesario
]
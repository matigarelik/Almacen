# AppAlmacen/urls.py
from django.urls import path
from AppAlmacen import views
from AppAlmacen import views_clases

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('clientes/', views.clientes, name='clientes'),
    path('buscar/', views.buscar, name='buscar'),
    # Agrega aquí más patrones de URL según sea necesario
]

urls_vistas_clases = [
    path('clases/lista/', views_clases.ProductoListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/', views_clases.ProductoDetalle.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.ProductoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>', views_clases.ProductoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>', views_clases.ProductoDeleteView.as_view(), name='Delete')
]

urlpatterns += urls_vistas_clases
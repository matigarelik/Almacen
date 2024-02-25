# AppAlmacen/urls.py
from django.urls import path
from AppAlmacen import views
from AppAlmacen import views_clases

urlpatterns = [
    path('', views.home, name="home"),
    #path('about/', views.about, name="About")
]

urlpatterns += [
    #path('', views.home, name='home'),
    path('almacen-productos/', views.productos, name='AlmacenProductos'),
    path('almacen-proveedores/', views.proveedores, name='AlmacenProveedores'),
    path('almacen-clientes/', views.clientes, name='AlmacenClientes'),
    path('almacen-buscar/', views.buscar, name='AlmacenBuscar'), ### ACA ESTA BUSCAR!!!!
    
]

urlpatterns += [
    path('producto-list/', views_clases.ProductoListView.as_view(), name='List'),
    path('producto-detail/<int:pk>/', views_clases.ProductoDetalle.as_view(), name='Detail'),
    path('producto-new/', views_clases.ProductoCreateView.as_view(), name='New'),
    path('producto-edit/<int:pk>', views_clases.ProductoUpdateView.as_view(), name='Edit'),
    path('producto-delete/<int:pk>', views_clases.ProductoDeleteView.as_view(), name='Delete')
    #path('buscar/', views.buscar, name='buscar')
]
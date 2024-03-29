# AppAlmacen/urls.py
from django.urls import path, include
from AppAlmacen import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="About")
]

urlpatterns += [
    path('cliente-list/', views.ClienteListView.as_view(), name='ClienteList'),
    path('cliente-detail/<int:pk>/', views.ClienteDetailView.as_view(), name='ClienteDetail'),
    path('cliente-edit/<int:pk>/', views.ClienteUpdateView.as_view(), name='ClienteEdit'),
    path('cliente-delete/<int:pk>/', views.ClienteDeleteView.as_view(), name='ClienteDelete'),
    path('cliente-create/', views.ClienteCreateView.as_view(), name='ClienteCreate'),
    path('cliente-buscar/', views.ClienteBuscar, name= 'ClienteBuscar')
]
# Producto
urlpatterns += [
    path('producto-list/', views.ProductoListView.as_view(), name='ProductoList'),
    path('producto-edit/<int:pk>/', views.ProductoUpdateView.as_view(), name='ProductoEdit'),
    path('producto-delete/<int:pk>/', views.ProductoDeleteView.as_view(), name='ProductoDelete'),
    path('producto-create/', views.ProductoCreateView.as_view(), name='ProductoCreate'),
    path('producto-buscar/', views.ProductoBuscar, name= 'ProductoBuscar')
    
]
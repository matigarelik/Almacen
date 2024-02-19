from django.shortcuts import render
from .models import Producto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductoListView(ListView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_list.html"


class ProductoDetalle(DetailView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_detalle.html"


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_form.html"
    success_url = reverse_lazy("List")
    fields = ["nombre", "descripcion"]


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_edit.html"
    #success_url = reverse_lazy("List")
    success_url = "/AppAlmacen/clases/lista/"
    fields = ["nombre", "descripcion"]


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy("List")
    template_name = "AppAlmacen/Vistas_Clases/producto_confirm_delete.html"


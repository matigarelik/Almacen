from django.shortcuts import render
from .models import Producto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductoDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_detail.html"


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_form.html"
    success_url = reverse_lazy("List")
    fields = ["nombre", "descripcion"]


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_edit.html"
    #success_url = reverse_lazy("List")
    success_url = "/AppAlmacen/clases/lista/"
    fields = ["nombre", "descripcion"]


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("List")
    template_name = "AppAlmacen/Vistas_Clases/producto_confirm_delete.html"


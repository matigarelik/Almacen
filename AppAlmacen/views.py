from django.shortcuts import render
from .models import Cliente, Producto
from AppAlmacen.forms import ClienteForm, BuscarForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente, Producto
from django.urls import reverse_lazy
from users.models import Imagen
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, "AppAlmacen/index.html")

@login_required
def about(request):
    return render(request, "AppCoder/about.html")

def buscar(request):
        if request.method == "POST":
             miFormulario = BuscarForm(request.POST)
             if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  cliente = Cliente.objects.filter(nombre__icontains=info["nombre"])
                  #render(request, "AppAlmacen/clientes.html", {"clientes":clientes})
                  return render(request, "AppAlmacen/resultado_buscar.html", {"formulario":miFormulario, "clientes":cliente})
        else:
            miFormulario = BuscarForm()
        return render(request, "AppAlmacen/buscar.html", {"formulario": miFormulario})   

# VISTA BASADA EN CLASES - PRODUCTO
class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
class ProductoDetailView(LoginRequiredMixin, DetailView):
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


# VISTA BASADA EN CLASES - CLIENTE
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_detail.html"

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_form.html"
    success_url = reverse_lazy("List")
    fields = ["nombre"]

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_edit.html"
    #success_url = reverse_lazy("List")
    success_url = "/AppAlmacen/clases/lista/"
    fields = ["nombre"]
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("List")
    template_name = "AppAlmacen/Vistas_Clases/cliente_confirm_delete.html"

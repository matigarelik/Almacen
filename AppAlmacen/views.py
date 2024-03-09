from django.shortcuts import redirect, render
from .models import Cliente, Producto, ProductoImagen
from .forms import ClienteForm, ClienteBuscarForm, ProductoBuscarForm, ProductosForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from users.models import Imagen
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models


def home(request):
    productos_oferta = Producto.objects.filter(oferta=True)
    return render(request, 'AppAlmacen/index.html', {'productos': productos_oferta})

@login_required
def about(request):
    productos_oferta = Producto.objects.filter(oferta=True)
    return render(request, 'AppAlmacen/index.html', {'productos': productos_oferta})

# BUSCAR CLIENTES
def ClienteBuscar(request):
    if request.method == "POST":
        miFormulario = ClienteBuscarForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            cliente = Cliente.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "AppAlmacen/Vistas_Clases/cliente_resultado_buscar.html", {"formulario": miFormulario, "clientes": cliente})
    else:
        miFormulario = ClienteBuscarForm()
    return render(request, "AppAlmacen/Vistas_Clases/cliente_buscar.html", {"formulario": miFormulario})   

# BUSCAR PRODUCTOS
def ProductoBuscar(request):
    if request.method == "POST":
        miFormulario = ProductoBuscarForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            producto = Producto.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "AppAlmacen/Vistas_Clases/producto_resultado_buscar.html", {"formulario": miFormulario, "productos": producto})
    else:
        miFormulario = ProductoBuscarForm()
    return render(request, "AppAlmacen/Vistas_Clases/producto_buscar.html", {"formulario": miFormulario})   

# VISTA BASADA EN CLASES - PRODUCTO
class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_list.html"

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_create.html"
    success_url = reverse_lazy("ProductoList")
    form_class = ProductosForm

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "AppAlmacen/Vistas_Clases/producto_edit.html"
    success_url = reverse_lazy("ProductoList")
    form_class = ProductosForm

    def get_initial(self):
        initial = super().get_initial()
        initial['oferta'] = self.object.oferta  # Establecer el estado actual de la oferta
        return initial

    def form_valid(self, form):
        producto = form.save(commit=False)
        
        # Verificar si el estado de la oferta ha cambiado
        if producto.oferta != self.object.oferta:
            if producto.oferta:
                # El producto se ha puesto en oferta
                # Aquí puedes realizar acciones adicionales si es necesario
                pass
            else:
                # El producto se ha sacado de oferta
                # Aquí puedes realizar acciones adicionales si es necesario
                pass
        return super().form_valid(form)

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("ProductoList")
    template_name = "AppAlmacen/Vistas_Clases/producto_confirm_delete.html"



# VISTA BASADA EN CLASES - CLIENTE
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_list.html"

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_detail.html"

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_create.html"
    success_url = reverse_lazy("ClienteList")
    fields = ["nombre", "telefono", "email"]

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_edit.html"
    success_url = reverse_lazy("ClienteList")
    #success_url = "/AppAlmacen/clases/cliente_list.html"
    fields = ["nombre", "email", "telefono"]

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("ClienteList")
    template_name = "AppAlmacen/Vistas_Clases/cliente_confirm_delete.html"

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "AppAlmacen/Vistas_Clases/cliente_create.html"
    success_url = reverse_lazy("ClienteList")
    fields = ["nombre", "email", "telefono"]
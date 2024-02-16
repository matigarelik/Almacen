# appstore/views.py
from django.shortcuts import render, redirect
from AppAlmacen.forms import ClienteForm, BuscarForm, ProductosForm, ProveedorForm
from AppAlmacen.models import Cliente, Producto, Proveedor


def home(request):
    return render(request, "AppAlmacen/index.html")

def productos(request):
    if request.method == "POST":
        miFormulario = ProductosForm(request.POST)

        if miFormulario.is_valid():  # Agregar paréntesis para llamar al método is_valid
                informacion = miFormulario.cleaned_data
                
                producto = Producto(nombre=informacion['nombre'], descripcion=informacion['descripcion'], precio=informacion['precio'])
                producto.save()
                # Redirigir a la página de clientes
                return redirect('productos')
    else:
        miFormulario = ProductosForm()
    return render(request, "AppAlmacen/productos.html", {"form": miFormulario})

def proveedores(request):
    if request.method == "POST":
        miFormulario = ProveedorForm(request.POST)

        if miFormulario.is_valid():  # Agregar paréntesis para llamar al método is_valid
                informacion = miFormulario.cleaned_data
                
                proveedor = Proveedor(nombre=informacion['nombre'], direccion=informacion['direccion'], telefono=informacion['telefono'])
                proveedor.save()
                # Redirigir a la página de clientes
                return redirect('proveedores')
    else:
        miFormulario = ProveedorForm()
    return render(request, "AppAlmacen/proveedores.html", {"form": miFormulario})

def clientes(request):
    if request.method == "POST":
        miFormulario = ClienteForm(request.POST)

        if miFormulario.is_valid():  # Agregar paréntesis para llamar al método is_valid
                informacion = miFormulario.cleaned_data
                # Guardar el cliente en la base de datos
                cliente = Cliente(nombre=informacion['nombre'], email=informacion['email'], telefono=informacion['telefono'])
                cliente.save()
                # Redirigir a la página de clientes
                return redirect('clientes')
                #return render(request, "AppAlmacen/clientes.html")
    else:
        # Renderizar el formulario para cargar nuevos clientes
        miFormulario = ClienteForm()
    return render(request, "AppAlmacen/clientes.html", {"form": miFormulario})

def buscar(request):
        if request.method == "POST":
             miFormulario = BuscarForm(request.POST)
             if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  cliente = Cliente.objects.filter(nombre__icontains=info["nombre"])
                  #render(request, "AppAlmacen/clientes.html", {"clientes":clientes})
                  return render(request, "AppAlmacen/buscar.html", {"formulario":miFormulario, "clientes":cliente})
        else:
            miFormulario = BuscarForm()
        return render(request, "AppAlmacen/buscar.html", {"formulario": miFormulario})    
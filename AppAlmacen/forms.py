from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)

class ProductosForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField()
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)

class ClienteBuscarForm(forms.Form):
    nombre = forms.CharField(max_length=100)

class ProductoBuscarForm(forms.Form):
    nombre = forms.CharField(max_length=100)
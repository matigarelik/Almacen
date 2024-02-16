from django.contrib import admin
from AppAlmacen.models import Producto
from AppAlmacen.models import Proveedor
from AppAlmacen.models import Cliente

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Cliente)
# Register your models here.

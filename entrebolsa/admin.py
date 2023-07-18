from django.contrib import admin
from .models import Categoria, Cliente,Minimarket, Producto, Reporte

admin.site.register(Cliente)
admin.site.register(Minimarket)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Reporte)

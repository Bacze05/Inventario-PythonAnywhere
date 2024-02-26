from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.forms import SelectDateWidget






from django.contrib import admin
from .models import Venta, DetalleVenta, Cajas

# Registra el modelo Venta en el panel de administración
admin.site.register(Venta)

# Registra el modelo DetalleVenta en el panel de administración
admin.site.register(DetalleVenta)
admin.site.register(Cajas)

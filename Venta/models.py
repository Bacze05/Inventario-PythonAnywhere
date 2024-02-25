from django.db import models
from django.conf import settings
from django.utils import timezone
from Inventario.models import Product, Descuento



# Create your models here.


class Cajas(models.Model):
    vendedor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    monto_inicial = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Monto Inicial")
    cantidad_vendida = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Cantidad Vendida")
    fecha_apertura = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Apertura")
    fecha_cierre = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Cierre")
    cerrada = models.BooleanField(default=False, verbose_name="Caja Cerrada")

    def __str__(self):
        return f"Caja {self.id} - {self.vendedor.username}"

    def abrir_caja(self):
        self.cerrada = False
        self.save()

    def cerrar_caja(self):
        self.cerrada = True
        self.fecha_cierre = timezone.now()
        self.save()
    @property
    def turno_abierto(self):
        return not self.cerrada
class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    caja = models.ForeignKey(Cajas, on_delete=models.CASCADE, default=1)
    # total_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Venta {self.id} - {self.fecha}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Product, related_name='detalles', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.ForeignKey(Descuento, on_delete=models.SET_NULL, null=True, blank=True)


    def calcular_subtotal(self):
        
        return self.precio * self.cantidad


class Reporte(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Reporte", db_index=True)
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción del Reporte")
    datos = models.JSONField(default=dict, verbose_name="Datos del Reporte")

    class Meta:
        indexes = [
            models.Index(fields=['nombre'], name='idx_nombre_length'),
        ]

    def __str__(self):
        return self.nombre



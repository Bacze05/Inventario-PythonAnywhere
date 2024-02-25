from django.urls import path
from .views import *

urlpatterns = [
        #VENTA
    path('apertura/', AbrirCajaView.as_view(), name="apertura"),
    path('cierre/', CerrarCajaView.as_view(), name="cierre"),
    path('panelVenta/', PanelVenta.as_view(), name="panelVenta"),
    path('listaVenta/', ListaVentaView.as_view(), name="listaVenta"),
]

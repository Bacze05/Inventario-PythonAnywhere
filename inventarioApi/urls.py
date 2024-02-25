from django.urls import path
from .views import *

urlpatterns = [
    #Prueba
    path('usuariosApi/', UsuarioApi, name='usuarioApi'),
    path('usuariosListApi/', usuario_listado, name='usuariolistApi'),
    path('productosListApi/', productos_listado, name='productolistApi'),
    path('usuariosListApi/<int:pk>/', usuario_detalle, name='usuariodetalleApi'),
]

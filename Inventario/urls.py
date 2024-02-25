from django.urls import path
from .views import *

urlpatterns = [
    path('categorias/',Categorias.as_view(), name="categorias"),
    path('proveedores/',ListaProveedores.as_view(), name='proveedores'),
    path('categorias/list/<str:nombre>/', ListaProductosView.as_view(), name="listaProductos"),
    path('productos/edit/<int:pk>',ProductoEdicion.as_view(),name='editarProducto'),
    path('categorias/edit/<int:pk>',CategoriaEdicion.as_view(),name='editarCategoria'),
    path('proveedor/edit/<int:pk>',ProveedorEdicion.as_view(),name='editarProveedor'),
    path('productos/eliminado/<int:pk>/',ProductoEliminar.as_view(),name='eliminarProducto'),
    path('categorias/eliminado/<int:pk>/',CategoriaEliminar.as_view(),name='eliminarCategoria'),
    path('proveedor/eliminado/<int:pk>/',ProveedorEliminar.as_view(),name='elimminarProveedor'),
]

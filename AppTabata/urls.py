from django.urls import path
from AppTabata import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #primera vista
    path('empleado',views.empleado, name="Empleado"),
    path('proveedor',views.proveedor, name="Proveedor"),
    path('producto',views.producto, name="Producto"),
    path('busqueda_producto',views.busquedaProducto, name="Busqueda_Producto"),
    path('buscar/',views.buscar, name="Resultado"),
]
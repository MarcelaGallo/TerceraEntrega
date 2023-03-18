from django.urls import path
from AppTabata import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"), #primera vista
    path('empleado',views.empleado, name="Empleado"),
    path('proveedor',views.proveedor, name="Proveedor"),
    path('producto',views.producto, name="Producto"),
    path('busqueda_producto',views.busquedaProducto, name="Busqueda_Producto"),
    path('buscar/',views.buscar, name="Resultado"),
    path('leerEmpleado', views.leerEmpleado, name='LeerEmpleado'),
    path('eliminarEmpleado/<empleado_nombre>/', views.eliminarEmpleado, name='EliminarEmpleado'),
    path('editarEmpleado/<empleado_nombre>/', views.editarEmpleado, name='EditarEmpleado'),
    path('producto/list', views.ProductoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ProductoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('logout', LogoutView.as_view(template_name='AppTabata/logout.html'), name='Logout'),
    path('about', views.about, name='About'),
]

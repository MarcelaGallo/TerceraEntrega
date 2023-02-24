from django.shortcuts import render
from django.http import HttpResponse
from AppTabata.models import *
from AppTabata.forms import *



# Create your views here.

def inicio(request):
    return render(request,'AppTabata/inicio.html')
   

def empleado(request):
    if request.method == 'POST':
        miFormulario = EmpleadoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
           informacion = miFormulario.cleaned_data
           empleado = Empleado(nombre=informacion['nombre'], apellido=informacion['apellido'], cargo=informacion['cargo'], activo=informacion['activo'])
           empleado.save()
        return render(request, "AppTabata/inicio.html")
    else:
        miFormulario = EmpleadoFormulario()
    return render(request, "AppTabata/empleado.html", {"miFormulario":miFormulario}) 


def proveedor(request):
    if request.method == 'POST':
        miFormulario = ProveedorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
           informacion = miFormulario.cleaned_data
           proveedor = Proveedor(nit=informacion['nit'], nombre=informacion['nombre'], ciudad=informacion['ciudad'], correo=informacion['correo'])
           proveedor.save()
        return render(request, "AppTabata/inicio.html")
    else:
        miFormulario = ProveedorFormulario()
    return render(request, "AppTabata/proveedor.html", {"miFormulario":miFormulario}) 


def producto(request):
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
           informacion = miFormulario.cleaned_data
           producto = Producto(codigo=informacion['codigo'], tipo=informacion['tipo'], referencia=informacion['referencia'], precio=informacion['precio'])
           producto.save()
        return render(request, "AppTabata/inicio.html")
    else:
        miFormulario = ProductoFormulario()
    return render(request, "AppTabata/producto.html", {"miFormulario":miFormulario}) 


def busquedaProducto(request):
    return render(request, "AppTabata/busquedaproducto.html")

def buscar(request):
    if request.GET["codigo"]:
        codigo = request.GET['codigo']
        producto = Producto.objects.filter(codigo__icontains=codigo)
        return render(request, "AppTabata/resultadoBusqueda.html", {"codigo":codigo, "producto":producto})
    else:
        respuesta = "No hay datos" 
    return HttpResponse(respuesta)


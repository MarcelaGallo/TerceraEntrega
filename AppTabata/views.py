from django.shortcuts import render
from django.http import HttpResponse
from AppTabata.models import *
from AppTabata.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from distutils.log import info


# Create your views here.

#def inicio(request):
    

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
    if request.GET[codigo]:
        codigo = request.GET['codigo']
        producto = Producto.objects.filter(codigo__contains=codigo)
        return render(request, "AppTabata/resultadoBusqueda.html", {"codigo":codigo, "producto":producto})
    else:
        respuesta = "No hay datos" 
    return HttpResponse(respuesta)

#CRUD PARA EMPLEADO
def leerEmpleado(request):
    empleado = Empleado.objects.all()
    contexto = {"Empleados" :empleado}
    return render(request, "AppTabata/leerEmpleado.html", contexto)

def eliminarEmpleado(request, empleado_nombre):
    empleado = Empleado.objects.get(nombre=empleado_nombre)
    empleado.delete()

    empleado = Empleado.objects.all()
    contexto = {"Empleados" :empleado}
    return render(request, "AppTabata/leerEmpleado.html", contexto)

def editarEmpleado(request, empleado_nombre):
    empleado = Empleado.objects.get(nombre=empleado_nombre)
    if request.method == 'POST':
         miFormulario = EmpleadoFormulario(request.POST)
         print(miFormulario)
         if miFormulario.is_valid:
               informacion = miFormulario.cleaned_data
           
               empleado.nombre = informacion['nombre']
               empleado.apellido = informacion['apellido']
               empleado.cargo = informacion['cargo']
               empleado.activo = informacion['activo']

               empleado.save()
               return render(request, "AppTabata/inicio.html")
    else:
         miFormulario = EmpleadoFormulario(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'cargo': empleado.cargo,'activo': empleado.activo})
    return render(request, "AppTabata/editarEmpleado.html", {"miFormulario":miFormulario, "empleado_nombre": empleado_nombre}) 

#CLASES CRUD PARA PRODUCTO
class ProductoList(ListView):
    model = Producto
    template_name = "AppTabata/producto_list.html"
    
class ProductoDetalle(DetailView):
    model = Producto
    template_name = "AppTabata/producto_detalle.html"
    
class ProductoCreacion(CreateView):
    model = Producto
    success_url = "/AppTabata/producto/list"
    fields = ['codigo', 'tipo', 'referencia','precio']

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = "/AppTabata/producto/list"
    fields = ['codigo', 'tipo', 'referencia','precio']
    
class ProductoDelete(DeleteView):
    model = Producto
    success_url = "/AppTabata/producto/list"


#LOGIN
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = contra)
            
            if user is not None:
                login(request, user)
                return render(request, "AppTabata/inicio.html", {"Mensaje":f"Bienvenido al Sistema {usuario}"})
            else:
                return render(request, "AppTabata/inicio.html", {"Mensaje":"Error, Datos Errados"})
        
        else:
            return render(request, "AppTabata/inicio.html", {"Mensaje":"Error, Formulario Incorrecto"})
    
    form = AuthenticationForm()
    return render(request, "AppTabata/login.html", {'form':form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
                
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppTabata/inicio.html", {"mensaje": "Usuario Creado Exitosamente: "})
    
    else:
        form = UserRegisterForm()
    
    return render(request, "AppTabata/registro.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditorForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.firstname = informacion['first_name']
            usuario.lastname = informacion['last_name']
            usuario.save()
            
            return render(request,"AppTabata/inicio.html", {'message': "El Usuario ha sido Actualizado."})
    else:

        inicial_data={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name}

        miFormulario = UserEditorForm(initial=inicial_data)
    
    return render(request, "AppTabata/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})



def about(request):
    funcionario = Empleado.objects.all()
    if funcionario:
        return render(request, "AppTabata/about.html", {'Funcionario':funcionario})
    else:
        return render(request, "AppTabata/about.html")
    
def blogempleado(request):
    return HttpResponse("Blog Empleado")
       

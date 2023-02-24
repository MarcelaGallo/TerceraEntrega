from django import forms


class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    cargo = forms.CharField(max_length=30)
    activo = forms.BooleanField()

class ProveedorFormulario(forms.Form):
    nit = forms.IntegerField()
    nombre = forms.CharField(max_length=40) 
    ciudad = forms.CharField(max_length=30)
    correo = forms.EmailField()

class ProductoFormulario(forms.Form):
    codigo = forms.IntegerField()
    tipo = forms.CharField(max_length=20) 
    referencia = forms.CharField(max_length=30)
    precio = forms.IntegerField()
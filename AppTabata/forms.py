from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#CLASES

#FORMULARIOS
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

#REGISTRO USUARIOS
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k: "" for k in fields}


class UserEditorForm(UserCreationForm):
    email=forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    first_name= forms.CharField(label='Nombre',required=False)
    last_name= forms.CharField(label='Apellido',required=False)

    class Meta:
        model = User
        fields = ['email', 'password1','password2','first_name', 'last_name']
        help_texts = {k:"" for k in fields}

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

   
class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cargo = models.CharField(max_length=30)
    activo = models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Cargo: {self.cargo} - Activo: {self.activo}"    

class Proveedor(models.Model):
    nit = models.IntegerField()
    nombre = models.CharField(max_length=40) 
    ciudad = models.CharField(max_length=30)
    correo = models.EmailField()

    def __str__(self): 
       return f"Nit: {self.nit} - Nombre: {self.nombre} - Ciudad: {self.ciudad} - Correo: {self.correo}" 

class Producto(models.Model):
    codigo = models.IntegerField()
    tipo = models.CharField(max_length=20) 
    referencia = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
       return f"Código: {self.codigo} - Tipo: {self.tipo} - Refencia: {self.referencia} - Precio: {self.precio}" 
    
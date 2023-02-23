from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cargo = models.CharField(max_length=30)
    activo = models.BooleanField()


class Proveedor(models.Model):
    nit = models.IntegerField()
    nombre = models.CharField(max_length=40) 
    ciudad = models.CharField(max_length=30)
    correo = models.EmailField()


class Producto(models.Model):
    codigo = models.IntegerField()
    tipo = models.CharField(max_length=20) 
    referencia = models.CharField(max_length=30)
    precio = models.IntegerField()

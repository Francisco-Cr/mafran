from django.db import models

class Ferreteria(models.Model):
    nombre = models.CharField(max_length=100)
    caracteristicas = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='ferreteria', null=True)
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=0)
    precio_unidad = models.DecimalField(default=0.00, max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.nombre}-{self.precio}-{self.imagen}"

class Adhesivo(models.Model):
    nombre = models.CharField(max_length=100)
    caracteristicas = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='adhesivos', null=True)
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=0)
    precio_unidad = models.DecimalField(default=0.00, max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.nombre}-{self.precio}-{self.imagen}"

class Aseo(models.Model):
    nombre = models.CharField(max_length=100)
    caracteristicas = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='aseo', null=True)
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=0)
    precio_unidad = models.DecimalField(default=0.00, max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.nombre}-{self.precio}-{self.imagen}"
from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    #CASCADE = borra el producto si se borra la categoria
    #PROTECT = no borra el producto si se borra la categoria
    #RESTRICT = no permite borrar el producto si se borra la categoria
    #SET_NULL = borra el producto si se borra la categoria y setea el valor a null
    #SET_DEFAULT = borra el producto si se borra la categoria y setea el valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
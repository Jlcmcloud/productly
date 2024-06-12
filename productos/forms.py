from . import models
from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria']
        exclude = ('creado_en',)
        labels = {
            'nombre': 'Nombre',
            'stock': 'Stock',
            'puntaje': 'Puntaje',
            'categoria': 'Categoria',
        }
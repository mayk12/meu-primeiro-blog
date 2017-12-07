from django.contrib import admin
from django import forms
from .models import Post
from .models import Categoria

admin.site.register(Post)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.fields['parent'].choices = categoria_pai_as_choices()

def categoria_pai_as_choices():
    categorias = []
    categorias.append(['', '-----------'])
    for categoria in Categoria.objects.filter(parent=None).all():
        categorias.append([categoria.id, categoria.nome])
    return categorias

class CategoriaAdmin(admin.ModelAdmin):
    form = CategoriaForm 

admin.site.register(Categoria, CategoriaAdmin)
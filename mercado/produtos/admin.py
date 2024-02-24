from django.contrib.admin import ModelAdmin, register

from mercado.produtos.models import Categoria, Departamento, Produto, Subcategoria


@register(Produto)
class ProdutoAdmin(ModelAdmin):
    list_display = ('nome', 'marca', 'subcategoria', 'data_criacao')
    list_filter = ('marca', 'subcategoria', 'subcategoria__categoria', 'subcategoria__categoria__departamento')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['nome']


@register(Subcategoria)
class SubcategoriaAdmin(ModelAdmin):
    list_display = ('nome', 'categoria', 'data_criacao')
    list_filter = ('categoria',)
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['nome']


@register(Categoria)
class CategoriaAdmin(ModelAdmin):
    list_display = ('nome', 'departamento', 'data_criacao')
    list_filter = ('departamento',)
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['nome']


@register(Departamento)
class DepartamentoAdmin(ModelAdmin):
    list_display = ('nome', 'data_criacao')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['nome']

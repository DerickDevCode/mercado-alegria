from django.contrib.admin import ModelAdmin, register


@register
class ProdutoAdmin(ModelAdmin):
    list_display = ('nome', 'marca', 'categoria', 'data_criacao')
    list_filter = ('marca', 'categoria')
    prepopulated_fields = {'slug': ('nome',)}


class CategoriaAdmin(ModelAdmin):
    list_display = ('nome', 'departamento', 'data_criacao')
    list_filter = ('departamento',)
    prepopulated_fields = {'slug': ('nome',)}


class DepartamentoAdmin(ModelAdmin):
    list_display = ('nome', 'data_criacao')
    prepopulated_fields = {'slug': ('nome',)}

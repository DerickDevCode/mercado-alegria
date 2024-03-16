from django.urls import path

from mercado.produtos.views import produto, pagina_de_marcas, pagina_de_departamentos, pagina_de_categorias, \
    pagina_de_subcategorias, pagina_de_pesquisa

app_name = 'produtos'
urlpatterns = [
    path('<slug:departamento>/<slug:categoria>/<slug:subcategoria>/<slug:slug>', produto, name='produto'),
    path('produtos-<str:marca>', pagina_de_marcas, name='pagina_de_marcas'),
    path('<slug:departamento>', pagina_de_departamentos, name='pagina_de_departamentos'),
    path('<slug:departamento>/<slug:categoria>', pagina_de_categorias, name='pagina_de_categorias'),
    path('<slug:departamento>/<slug:categoria>/<slug:subcategoria>', pagina_de_subcategorias,
         name='pagina_de_subcategorias'),
    path('search/', pagina_de_pesquisa, name='pagina_de_pesquisa'),
]

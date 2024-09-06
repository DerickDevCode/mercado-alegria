from django.urls import path

from mercado.produtos.views import produto, pagina_de_marcas, pagina_de_departamentos, pagina_de_categorias, \
    pagina_de_subcategorias, pagina_de_pesquisa, pagina_do_carrinho, adicionar_ao_carrinho, remover_do_carrinho, \
    excluir_do_carrinho, pagina_dos_favoritos, adicionar_aos_favoritos, remover_dos_favoritos

app_name = 'produtos'
urlpatterns = [
    path('<slug:departamento>/<slug:categoria>/<slug:subcategoria>/<slug:slug>', produto, name='produto'),
    path('produtos-<str:marca>', pagina_de_marcas, name='pagina_de_marcas'),
    path('<slug:departamento>', pagina_de_departamentos, name='pagina_de_departamentos'),
    path('<slug:departamento>/<slug:categoria>', pagina_de_categorias, name='pagina_de_categorias'),
    path('<slug:departamento>/<slug:categoria>/<slug:subcategoria>', pagina_de_subcategorias,
         name='pagina_de_subcategorias'),
    path('search/', pagina_de_pesquisa, name='pagina_de_pesquisa'),
    path('carrinho/', pagina_do_carrinho, name='pagina_do_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:produto_id>/', remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/excluir/<int:produto_id>/', excluir_do_carrinho, name='excluir_do_carrinho'),
    path('favoritos/', pagina_dos_favoritos, name='pagina_dos_favoritos'),
    path('favoritos/adicionar/<int:produto_id>/', adicionar_aos_favoritos, name='adicionar_aos_favoritos'),
    path('favoritos/remover/<int:produto_id>/', remover_dos_favoritos, name='remover_dos_favoritos'),
]

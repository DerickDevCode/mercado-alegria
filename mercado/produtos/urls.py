from django.urls import path

from mercado.produtos.views import produto, pagina_de_marcas

app_name = 'produtos'
urlpatterns = [
    path('<slug:departamento>/<slug:categoria>/<slug:slug>', produto, name='produto'),
    path('produtos-<slug:marca>', pagina_de_marcas, name='pagina_de_marcas'),
]

from django.shortcuts import render

from mercado.produtos import facade


def produto(request, departamento, categoria, slug):
    departamento = facade.buscar_departamento_da_categoria(slug)
    categoria = facade.buscar_categoria_do_produto(slug)
    produto = facade.buscar_produto(slug)
    return render(request, 'produtos/produto_detalhe.html',
                  context={'departamento': departamento, 'categoria': categoria, 'produto': produto})

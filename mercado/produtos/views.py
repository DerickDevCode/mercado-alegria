from django.shortcuts import render

from mercado.produtos import facade


def produto(request, departamento, categoria, slug):
    departamento = facade.buscar_departamento_da_categoria(slug)
    categoria = facade.buscar_categoria_do_produto(slug)
    produto = facade.buscar_produto(slug)
    return render(request, 'produtos/produto_detalhe.html',
                  context={'departamento': departamento, 'categoria': categoria, 'produto': produto})


def pagina_de_marcas(request, marca):
    produtos = facade.listar_produtos_por_marca(marca)
    marca = produtos[0].marca
    return render(request, 'produtos/produtos_por_marca.html', context={'produtos': produtos, 'marca': marca})


def pagina_de_departamentos(request, departamento):
    produtos = facade.listar_produtos_por_departamento(departamento)
    departamento = produtos[0].categoria.departamento.nome
    return render(request, 'produtos/produtos_por_departamento.html',
                  context={'produtos': produtos, 'departamento': departamento})

from django.shortcuts import render

from mercado.produtos import facade
from mercado.produtos.carrinho import calcular_total_itens, obter_carrinho_e_itens, \
    adicionar_produto_ao_carrinho, remover_produto_do_carrinho, excluir_produto_do_carrinho


def produto(request, departamento, categoria, subcategoria, slug):
    departamento = facade.buscar_departamento_do_produto(slug)
    categoria = facade.buscar_categoria_do_produto(slug)
    subcategoria = facade.buscar_subcategoria_do_produto(slug)
    produto = facade.buscar_produto(slug)
    marca = produto.marca
    return render(request, 'produtos/produto_detalhe.html',
                  context={'departamento': departamento, 'categoria': categoria, 'subcategoria': subcategoria,
                           'produto': produto, 'marca': marca})


def pagina_de_departamentos(request, departamento):
    produtos = facade.listar_produtos_por_departamento(departamento)
    departamento = produtos[0].subcategoria.categoria.departamento.nome
    return render(request, 'produtos/produtos_por_departamento.html',
                  context={'produtos': produtos, 'departamento': departamento})


def pagina_de_subcategorias(request, departamento, categoria, subcategoria):
    produtos = facade.listar_produtos_por_subcategoria(subcategoria)
    subcategoria = produtos[0].subcategoria.nome
    return render(request, 'produtos/produtos_por_subcategoria.html',
                  context={'produtos': produtos, 'subcategoria': subcategoria})


def pagina_de_categorias(request, departamento, categoria):
    produtos = facade.listar_produtos_por_categoria(categoria)
    categoria = produtos[0].subcategoria.categoria.nome
    return render(request, 'produtos/produtos_por_categoria.html',
                  context={'produtos': produtos, 'categoria': categoria})


def pagina_de_marcas(request, marca):
    produtos = facade.listar_produtos_por_marca(marca)
    return render(request, 'produtos/produtos_por_marca.html',
                  context={'produtos': produtos, 'marca': marca})


def pagina_de_pesquisa(request):
    query = request.GET.get('search')
    produtos = facade.filtrar_produtos_pela_pesquisa(query)
    return render(request, 'produtos/produtos_por_pesquisa.html',
                  context={'produtos': produtos})


def pagina_do_carrinho(request):
    carrinho, carrinhoitens = obter_carrinho_e_itens(request)
    total = calcular_total_itens(carrinhoitens)
    return render(request, 'produtos/carrinho.html',
                  context={'carrinho': carrinho, 'carrinhoitens': carrinhoitens, 'total': total})


def adicionar_ao_carrinho(request, produto_id: int):
    carrinho, carrinhoitens = adicionar_produto_ao_carrinho(request, produto_id)
    total = calcular_total_itens(carrinhoitens)
    return render(request, 'produtos/carrinho.html',
                  context={'carrinho': carrinho, 'carrinhoitens': carrinhoitens, 'total': total})


def remover_do_carrinho(request, produto_id: int):
    carrinho, carrinhoitens = remover_produto_do_carrinho(request, produto_id)
    total = calcular_total_itens(carrinhoitens)
    return render(request, 'produtos/carrinho.html',
                  context={'carrinho': carrinho, 'carrinhoitens': carrinhoitens, 'total': total})


def excluir_do_carrinho(request, produto_id: int):
    carrinho, carrinhoitens = excluir_produto_do_carrinho(request, produto_id)
    total = calcular_total_itens(carrinhoitens)
    return render(request, 'produtos/carrinho.html',
                  context={'carrinho': carrinho, 'carrinhoitens': carrinhoitens, 'total': total})

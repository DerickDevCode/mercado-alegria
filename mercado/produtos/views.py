from django.shortcuts import render

from mercado.produtos import facade
from mercado.produtos.models import Produto, CarrinhoItem


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
    carrinho = facade.buscar_carrinho_existente(request)
    if not carrinho:
        carrinho = facade.criar_carrinho(request)
    return render(request, 'produtos/carrinho.html', context={'carrinho': carrinho})


def adicionar_ao_carrinho(request, produto_id: int):
    carrinho = facade.buscar_carrinho_existente(request)
    if not carrinho:
        carrinho = facade.criar_carrinho(request)

    produto = Produto.objects.get(id=produto_id)

    try:
        item = facade.buscar_item_do_carrinho(produto)
        item.quantidade += 1
        item.save()
    except Exception:
        novo_item = CarrinhoItem(produto=produto, carrinho=carrinho)
        novo_item.save()
    return render(request, 'produtos/carrinho.html', context={'carrinho': carrinho})


def remover_do_carrinho(request, produto_id: int):
    carrinho = facade.buscar_carrinho_existente(request)
    if not carrinho:
        carrinho = facade.criar_carrinho(request)

    produto = Produto.objects.get(id=produto_id)

    try:
        item = facade.buscar_item_do_carrinho(produto)
        item.quantidade -= 1
        item.save()
        if item.quantidade <= 0:
            item.delete()
    except Exception:
        return render(request, 'produtos/carrinho.html', context={'carrinho': carrinho})
    return render(request, 'produtos/carrinho.html', context={'carrinho': carrinho})


def excluir_do_carrinho(request, produto_id: int):
    carrinho = facade.buscar_carrinho_existente(request)
    if not carrinho:
        carrinho = facade.criar_carrinho(request)

    produto = Produto.objects.get(id=produto_id)

    try:
        item = facade.buscar_item_do_carrinho(produto)
        item.delete()
    except Exception:
        return render(request, 'produtos/carrinho.html', context={'carrinho': carrinho})
    return render(request, 'produtos/carrinho.html', context={'carrinho': carrinho})

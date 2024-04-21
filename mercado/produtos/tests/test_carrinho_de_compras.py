import pytest
from django.urls import reverse

from mercado.produtos.carrinho import Carrinho
from mercado.produtos.models import Produto, Departamento, Categoria, Subcategoria


@pytest.fixture
def departamento(db):
    return Departamento.objects.create(nome='Teste', slug='teste')


@pytest.fixture
def categoria(departamento):
    return Categoria.objects.create(nome='Teste', slug='teste', departamento=departamento)


@pytest.fixture
def subcategoria(categoria):
    return Subcategoria.objects.create(nome='Teste', slug='teste', categoria=categoria)


@pytest.fixture
def produto1(subcategoria):
    return Produto.objects.create(nome='Produto1', slug=produto1, marca='teste', codigo=0000, preco=10.50,
                                  imagem='mediafiles/imagens_produtos/arroz-bernardo.jpg',
                                  descricao='texto aleatório para testes', subcategoria=subcategoria)


@pytest.fixture
def produto2(subcategoria):
    return Produto.objects.create(nome='Produto2', slug=produto2, marca='teste', codigo=9999, preco=20.50,
                                  imagem='mediafiles/imagens_produtos/arroz-bernardo.jpg',
                                  descricao='texto aleatório para testes', subcategoria=subcategoria)


@pytest.fixture
def carrinho(client, db):
    return Carrinho(request=client)


@pytest.fixture
def resp(client, carrinho):
    resp = client.get(reverse('produtos:pagina_do_carrinho', ))
    return resp


# ----------------------------------------------INÍCIO DOS TESTES----------------------------------------------
def test_status_code(resp):
    assert resp.status_code == 200


def test_funcao_add_product_to_cart(resp, carrinho, produto1):
    carrinho.add_product_to_cart(produto=produto1, quantidade=1)
    assert len(carrinho.carrinho) == 1
    assert carrinho.carrinho[str(produto1.id)]['quantidade'] == 1


def test_funcao_remove_product_from_cart_com_mais_de_uma_quantidade(resp, carrinho, produto1):
    carrinho.add_product_to_cart(produto=produto1, quantidade=2)
    carrinho.remove_product_from_cart(produto=produto1)
    assert len(carrinho.carrinho) == 1
    assert carrinho.carrinho[str(produto1.id)]['quantidade'] == 1


def test_funcao_remove_product_from_cart_com_apenas_uma_quantidade(resp, carrinho, produto1):
    carrinho.add_product_to_cart(produto=produto1, quantidade=1)
    carrinho.remove_product_from_cart(produto=produto1)
    assert len(carrinho.carrinho) == 0


def test_funcao_exclude_product_from_cart(resp, carrinho, produto1, produto2):
    carrinho.add_product_to_cart(produto=produto1, quantidade=3)
    carrinho.exclude_product_from_cart(produto=produto1)
    assert len(carrinho.carrinho) == 0


def test_funcao_get_products(resp, carrinho, produto1, produto2):
    carrinho.add_product_to_cart(produto=produto1, quantidade=1)
    carrinho.add_product_to_cart(produto=produto2, quantidade=2)
    produtos = carrinho.get_products()
    assert len(produtos) == 2

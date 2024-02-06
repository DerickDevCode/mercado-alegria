import pytest
from django.urls import reverse
from model_bakery import baker

from mercado.base.django_assertions import assert_contains
from mercado.produtos.models import Departamento, Categoria, Produto


@pytest.fixture
def departamento(db):
    return baker.make(Departamento)


@pytest.fixture
def categoria(departamento):
    return baker.make(Categoria, departamento=departamento)


@pytest.fixture
def produto(categoria):
    return baker.make(Produto, categoria=categoria, preco=20.75, descricao='texto aleatório para testes',
                      imagem='mediafiles/imagens_produtos/arroz-bernardo.jpg')


@pytest.fixture
def resp(client, departamento, categoria, produto):
    resp = client.get(reverse('produtos:produto',
                              kwargs={'departamento': produto.categoria.departamento.slug,
                                      'categoria': produto.categoria.slug,
                                      'slug': produto.slug}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_nome_produto(resp, produto):
    assert_contains(resp, f'<h5 class="mt-3"><b>{produto.nome}</b></h5>')


def test_marca_produto(resp, produto):
    assert_contains(resp, f'<a class="text-reset text-decoration-none" href="#">{produto.marca}</a>')


def test_codigo_produto(resp, produto):
    assert_contains(resp, f'<small>(Código: {produto.codigo})</small>')


def test_preco_produto(resp, produto):
    assert_contains(resp, f'<h2 class="text-success"><b>R$ {str(produto.preco).replace(".", ",")}</b></h2>')


def test_descricao_produto(resp, produto):
    assert_contains(resp, f'<h6>{produto.descricao}</h6>')

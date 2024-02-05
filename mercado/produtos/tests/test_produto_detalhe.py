import pytest
from django.urls import reverse
from model_bakery import baker

from mercado.produtos.models import Departamento, Categoria, Produto


@pytest.fixture
def departamento(db):
    return baker.make(Departamento)


@pytest.fixture
def categoria(departamento, db):
    return baker.make(Categoria, departamento=departamento)


@pytest.fixture
def produto(categoria, db):
    return baker.make(Produto, categoria=categoria)


@pytest.fixture
def resp(client, departamento, categoria, produto):
    resp = client.get(reverse('produtos:produto',
                              kwargs={'departamento': produto.categoria.departamento.slug,
                                      'categoria': produto.categoria.slug,
                                      'slug': produto.slug}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200

#
# def test_nome_produto(resp):
#     pass
#
#
# def test_marca_produto(resp):
#     pass
#
#
# def test_codigo_produto(resp):
#     pass
#
#
# def test_preco_produto(resp):
#     pass
#
#
# def test_descricao_produto(resp):
#     pass

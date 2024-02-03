import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('produtos:produto'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_nome_produto(resp):
    pass


def test_marca_produto(resp):
    pass


def test_codigo_produto(resp):
    pass


def test_preco_produto(resp):
    pass


def test_descricao_produto(resp):
    pass

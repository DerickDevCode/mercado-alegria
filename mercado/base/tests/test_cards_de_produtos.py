import pytest
from django.urls import reverse
from model_bakery import baker

from mercado.base.django_assertions import assert_contains
from mercado.produtos.models import Produto, Departamento, Categoria


@pytest.fixture
def departamento(db):
    return baker.make(Departamento)


@pytest.fixture
def categoria(departamento):
    return baker.make(Categoria, departamento=departamento)


@pytest.fixture
def produtos(categoria):
    return baker.make(Produto, 6, categoria=categoria, preco=20.75, descricao='texto aleatório para testes',
                      imagem='mediafiles/imagens_produtos/arroz-bernardo.jpg')


@pytest.fixture
def resp(client, produtos):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_imagem_produto(resp, produtos):
    for produto in produtos:
        assert_contains(resp, f'src="{produto.imagem.url}"')


def test_nome_produto(resp, produtos):
    for produto in produtos:
        assert_contains(resp, f'<p class="card-text text-muted">{produto.nome}</p>')


def test_preco_produto(resp, produtos):
    for produto in produtos:
        assert_contains(resp,
                        f'<h5 class="card-title text-success"><b>R$ {str(produto.preco).replace(".", ",")}</b></h5>')


def test_link_do_produto_na_imagem_e_nome(resp, produtos):
    for produto in produtos:
        assert_contains(resp, f'<a class="text-decoration-none ratio ratio-1x1" href="{produto.get_absolute_url()}">')
        assert_contains(resp, f'<a class="text-decoration-none" href="{produto.get_absolute_url()}">')

# Adicionar esse teste quando a funcionalidade do carrinho for implementada.
# def test_botao_de_adicionar_o_produto_ao_carrinho(resp):
#     pass

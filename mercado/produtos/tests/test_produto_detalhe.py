import pytest
from django.urls import reverse
from model_bakery import baker

from mercado.django_assertions import assert_contains
from mercado.produtos.models import Departamento, Categoria, Produto, Subcategoria


@pytest.fixture
def departamento(db):
    return baker.make(Departamento)


@pytest.fixture
def categoria(departamento):
    return baker.make(Categoria, departamento=departamento)


@pytest.fixture
def subcategoria(categoria):
    return baker.make(Subcategoria, categoria=categoria)


@pytest.fixture
def produto(subcategoria):
    return baker.make(Produto, subcategoria=subcategoria, preco=20.75, descricao='texto aleatório para testes',
                      imagem='mediafiles/imagens_produtos/arroz-bernardo.jpg')


@pytest.fixture
def resp(client, departamento, categoria, produto):
    resp = client.get(reverse('produtos:produto',
                              kwargs={'departamento': produto.subcategoria.categoria.departamento.slug,
                                      'categoria': produto.subcategoria.categoria.slug,
                                      'subcategoria': produto.subcategoria.slug,
                                      'slug': produto.slug}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_imagem_produto(resp, produto):
    assert_contains(resp, f'src="{produto.imagem.url}"')


def test_nome_produto(resp, produto):
    assert_contains(resp, f'<h4 class="mt-3"><b>{produto.nome}</b></h4>')


def test_marca_produto(resp, produto):
    assert_contains(resp, f'''>
                                {produto.marca}
                            </a>''')


def test_link_para_pagina_de_marca_dos_produtos(resp, produto):
    assert_contains(resp,
                    f'''href="{reverse("produtos:pagina_de_marcas",
                                       kwargs={"marca": produto.marca})}">''')


def test_codigo_produto(resp, produto):
    assert_contains(resp, f'''small>
                                (Código: {produto.codigo})
                            </small>''')


def test_preco_produto(resp, produto):
    assert_contains(resp, f'''<b>
                                R$ {str(produto.preco).replace(".", ",")}
                            </b>''')


def test_descricao_produto(resp, produto):
    assert_contains(resp, f'<h6>{produto.descricao}</h6>')


def test_guia_de_pagina_departamento(resp, produto):
    assert_contains(resp,
                    f'''>
                        {produto.subcategoria.categoria.departamento.nome}</a></li>''')


def test_link_da_guia_para_pagina_de_departamento_dos_produto(resp, produto):
    assert_contains(resp,
                    f'''<li class="breadcrumb-item"><a
                            href="{produto.subcategoria.categoria.departamento.get_absolute_url()}">'''
                    )


def test_guia_de_pagina_categoria(resp, produto):
    assert_contains(resp, f'''>
                        {produto.subcategoria.categoria.nome}</a></li>''')


def test_link_da_guia_para_pagina_de_categoria_dos_produto(resp, produto):
    assert_contains(resp,
                    f'''<li class="breadcrumb-item"><a href="{produto.subcategoria.categoria.get_absolute_url()}">'''
                    )


def test_guia_de_pagina_subcategoria(resp, produto):
    assert_contains(resp, f'''>
                        {produto.subcategoria.nome}</a></li>''')


def test_link_da_guia_para_pagina_de_subcategoria_dos_produto(resp, produto):
    assert_contains(resp,
                    f'''<li class="breadcrumb-item"><a href="{produto.subcategoria.get_absolute_url()}">'''
                    )

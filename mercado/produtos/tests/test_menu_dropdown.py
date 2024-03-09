from itertools import cycle

import pytest
from django.urls import reverse
from model_bakery import baker

from mercado.base.django_assertions import assert_contains
from mercado.produtos.models import Departamento, Categoria, Subcategoria


@pytest.fixture
def departamentos(db):
    return baker.make(Departamento, 5)


@pytest.fixture
def categorias(departamentos):
    return baker.make(Categoria, 3, departamento=cycle(departamentos))


@pytest.fixture
def subcategorias(categorias):
    return baker.make(Subcategoria, 3, categoria=cycle(categorias))


@pytest.fixture
def resp(client, departamentos, categorias, subcategorias):
    resp = client.get(reverse('base:home'))
    return resp


def test_exibicao_de_departamentos(resp, departamentos):
    for departamento in departamentos:
        assert_contains(resp, f'''<a class="dropdown-item"
                                               href="{departamento.get_absolute_url()}">
                                                {departamento.nome}
                                            </a>''')

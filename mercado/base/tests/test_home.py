import pytest
from django.urls import reverse

from mercado.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Comercial Alegria</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}"')


def test_favicon(resp):
    assert_contains(resp, 'href="/static/img/favicon.webp"')


def test_logo_rodape(resp):
    assert_contains(resp, 'src="/static/img/banner.webp"')


@pytest.fixture
def resp_home_com_usuario_logado(client_com_usuario_logado):
    return client_com_usuario_logado.get(reverse('base:home'))


def test_icone_do_usuario_logado(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, f'<a class="navbar-brand" href="{reverse("base:perfil")}">')

# Adicionar teste para a lista de produtos no dropdown.

import pytest
from django.urls import reverse

from mercado.base.django_assertions import assert_contains


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

# # descomentar quando implementar o favicon definitivo
# def test_favicon(resp):
#     assert_contains(resp, 'href="/static/img/usuario_icon"')
#
# descomentar quando implementar o link e o botão da página definitivo
# def test_login_link_e_botao(resp):
#     assert_contains(resp, 'href="<link da página de cadastro de usuário>"')
#     assert_contains(resp, 'src="/static/img/usuario_icon_3"')
#
# descomentar quando implementar o logo do rodapé definitivo
# def test_logo_rodape(resp):
#     assert_contains(resp, 'src="/static/img/usuario_icon"')

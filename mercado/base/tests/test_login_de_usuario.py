import pytest
from django.urls import reverse

from mercado.base.models import User
from mercado.django_assertions import assert_contains


@pytest.fixture
def resp_get_login(client, db):
    return client.get(reverse('login'))


def test_status_code(resp_get_login):
    assert resp_get_login.status_code == 200


def test_input_email_esta_presente_na_pagina(resp_get_login):
    assert_contains(resp_get_login, '<input type="email" name="username"')


def test_input_senha_esta_presente_na_pagina(resp_get_login):
    assert_contains(resp_get_login, '<input type="password" name="password"')


@pytest.fixture
def usuario(db):
    usuario_modelo = User.objects.create_user(first_name='teste', last_name='testando', date_of_birth='2000-01-01',
                                              email='usuario@exemplo.com',
                                              cpf='000.000.000-00', phone_number='00 00000-0000', password='teste')
    senha = 'teste'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_post_login(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_redirect_login_para_a_home(resp_post_login):
    assert resp_post_login.status_code == 302
    assert resp_post_login.url == reverse('base:home')

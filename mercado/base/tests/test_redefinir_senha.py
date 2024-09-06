import pytest
from django.urls import reverse

from mercado.base.models import User
from mercado.django_assertions import assert_contains


@pytest.fixture
def resp_alterar_senha_com_usuario_logado(client_com_usuario_logado):
    return client_com_usuario_logado.get(reverse('password_change'))


def test_status_code(resp_alterar_senha_com_usuario_logado):
    assert resp_alterar_senha_com_usuario_logado.status_code == 200


# ------------------------ Testes do Front-end ------------------------ #


def test_input_senha_antiga_esta_presente_na_pagina(resp_alterar_senha_com_usuario_logado):
    assert_contains(resp_alterar_senha_com_usuario_logado, '<input type="password" name="old_password"')


def test_input_nova_senha_esta_presente_na_pagina(resp_alterar_senha_com_usuario_logado):
    assert_contains(resp_alterar_senha_com_usuario_logado, '<input type="password" name="new_password1"')


def test_input_confirmar_nova_senha_esta_presente_na_pagina(resp_alterar_senha_com_usuario_logado):
    assert_contains(resp_alterar_senha_com_usuario_logado, '<input type="password" name="new_password2"')


# ------------------------ Testes do Back-end ------------------------ #

@pytest.fixture
def usuario_para_testar_senhas(db):
    usuario = User.objects.create_user(first_name='teste', last_name='testando', date_of_birth='2000-01-01',
                                       email='usuario@gmail.com',
                                       cpf='123.000.000-00', phone_number='00 00000-0000', password='senha_antiga123')
    return usuario


def test_senha_alterada_com_sucesso(usuario_para_testar_senhas, client):
    client.login(username=usuario_para_testar_senhas.email, password='senha_antiga123')
    resp = client.post(reverse('password_change'),
                       {'old_password': 'senha_antiga123',
                        'new_password1': 'nova_senha123',
                        'new_password2': 'nova_senha123'})
    assert resp.status_code == 302
    assert resp.url == reverse('password_change_done')


def test_login_com_senha_antiga_nao_deve_ser_possivel(usuario_para_testar_senhas, client):
    client.login(username=usuario_para_testar_senhas.email, password='senha_antiga123')
    client.post(reverse('password_change'),
                {'old_password': 'senha_antiga123',
                 'new_password1': 'nova_senha123',
                 'new_password2': 'nova_senha123'})
    client.logout()
    assert client.login(username=usuario_para_testar_senhas.email, password='senha_antiga123') is False


def test_login_com_senha_nova_deve_ser_possivel(usuario_para_testar_senhas, client):
    client.login(username=usuario_para_testar_senhas.email, password='senha_antiga123')
    client.post(reverse('password_change'),
                {'old_password': 'senha_antiga123',
                 'new_password1': 'nova_senha123',
                 'new_password2': 'nova_senha123'})
    client.logout()
    assert client.login(username=usuario_para_testar_senhas.email, password='nova_senha123') is True

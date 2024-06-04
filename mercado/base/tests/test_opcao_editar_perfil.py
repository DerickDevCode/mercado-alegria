import pytest
from django.urls import reverse

from mercado.base.models import User
from mercado.django_assertions import assert_contains


@pytest.fixture
def resp_editar_perfil_com_usuario_logado(client_com_usuario_logado):
    return client_com_usuario_logado.get(reverse('base:editar_perfil'))


def test_status_code(resp_editar_perfil_com_usuario_logado):
    assert resp_editar_perfil_com_usuario_logado.status_code == 200


# ------------------------ Testes do Front-end ------------------------ #


def test_input_nome_esta_presente_na_pagina(resp_editar_perfil_com_usuario_logado):
    assert_contains(resp_editar_perfil_com_usuario_logado, '<input type="text" name="first_name"')


def test_input_sobrenome_esta_presente_na_pagina(resp_editar_perfil_com_usuario_logado):
    assert_contains(resp_editar_perfil_com_usuario_logado, '<input type="text" name="last_name"')


def test_input_data_de_nascimento_esta_presente_na_pagina(resp_editar_perfil_com_usuario_logado):
    assert_contains(resp_editar_perfil_com_usuario_logado, '<input type="date" name="date_of_birth"')


def test_input_email_esta_presente_na_pagina(resp_editar_perfil_com_usuario_logado):
    assert_contains(resp_editar_perfil_com_usuario_logado, '<input type="email" name="email"')


def test_input_cpf_esta_presente_na_pagina(resp_editar_perfil_com_usuario_logado):
    assert_contains(resp_editar_perfil_com_usuario_logado, '<input type="text" name="cpf"')


def test_input_numero_de_telefone_esta_presente_na_pagina(resp_editar_perfil_com_usuario_logado):
    assert_contains(resp_editar_perfil_com_usuario_logado, '<input type="text" name="phone_number"')


def test_input_senha_esta_presente_na_pagina(resp_editar_perfil_com_usuario_logado):
    assert_contains(resp_editar_perfil_com_usuario_logado, '<input type="password" name="password"')


@pytest.fixture
def resp_usuario_editado(client_com_usuario_logado):
    return client_com_usuario_logado.post(reverse('base:editar_perfil'),
                                          {'first_name': 'perfil alterado com sucesso',
                                           'last_name': 'alteração concluída',
                                           'date_of_birth': '01/01/2000',
                                           'email': 'teste@gmail.com',
                                           'cpf': '123.456.789-00',
                                           'phone_number': '00 00000-0000',
                                           'password': 'testando123'})


def test_alteracoes_feitas_no_perfil_do_usuario_foram_salvas_com_sucesso(resp_usuario_editado):
    user = User.objects.get(email='teste@gmail.com')
    assert user.first_name == 'perfil alterado com sucesso'
    assert user.last_name == 'alteração concluída'
    assert user.cpf == '123.456.789-00'

import pytest
from django.urls import reverse

from mercado.base.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('base:cadastro'))


def test_status_code(resp):
    assert resp.status_code == 200


# ------------------------ Testes do Front-end ------------------------ #

def test_icone_do_usuario_com_palavra_default(resp):
    assert_contains(resp, '''<img src="/static/img/usuario_icon_3.png" alt="Usuario" width="36" height="30">
                                <small>Conecte-se</small>
                            ''')


def test_botao_e_link_entrar_esta_presente_no_dropdown_do_usuario(resp):
    assert_contains(resp, f'<a class="dropdown-item" href="{reverse("login")}">Entrar</a>')


def test_botao_e_link_cadastrar_esta_presente_no_dropdown_do_usuario(resp):
    assert_contains(resp, f'<a class="dropdown-item" href="{reverse("base:cadastro")}">Cadastrar-se</a>')


def test_input_nome_esta_presente_na_pagina(resp):
    assert_contains(resp, '<input type="text" name="first_name"')


def test_input_sobrenome_esta_presente_na_pagina(resp):
    assert_contains(resp, '<input type="text" name="last_name"')


def test_input_data_de_nascimento_esta_presente_na_pagina(resp):
    assert_contains(resp, '<input type="text" name="date_of_birth"')


def test_input_email_esta_presente_na_pagina(resp):
    assert_contains(resp, '<input type="email" name="email"')


def test_input_cpf_esta_presente_na_pagina(resp):
    assert_contains(resp, '<input type="text" name="cpf"')


def test_input_numero_de_telefone_esta_presente_na_pagina(resp):
    assert_contains(resp, '<input type="text" name="phone_number"')


def test_input_senha_esta_presente_na_pagina(resp):
    assert_contains(resp, '<input type="password" name="password"')

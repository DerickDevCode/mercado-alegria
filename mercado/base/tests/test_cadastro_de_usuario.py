import pytest
from django.urls import reverse

from mercado.django_assertions import assert_contains
from mercado.base.models import User


@pytest.fixture
def resp(client, db):
    return client.get(reverse('base:cadastro'))


def test_status_code(resp):
    assert resp.status_code == 200


# ------------------------ Testes do Front-end ------------------------ #

def test_icone_do_usuario_deslogado(resp):
    assert_contains(resp, '''<a class="navbar-brand" data-bs-toggle="dropdown" aria-expanded="false"
                               href="#">
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


# ------------------------ Testes do Back-end ------------------------ #

@pytest.fixture
def resp_post_cadastro(client, db):
    return client.post(reverse('base:cadastro'), {'first_name': 'teste cadastro', 'last_name': 'cadastrando',
                                                  'date_of_birth': '2000-01-01',
                                                  'email': 'teste_criacao_usuario@gmail.com',
                                                  'cpf': '123.456.789-00',
                                                  'phone_number': '000.000.000-00',
                                                  'password': 'teste'})


def test_confirmacao_de_usuario_criado_apos_cadastro(resp_post_cadastro):
    assert User.objects.get(
        email='teste_criacao_usuario@gmail.com').email == 'teste_criacao_usuario@gmail.com'

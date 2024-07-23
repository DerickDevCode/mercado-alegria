from django.urls import path

from mercado.base.views import home, cadastro, perfil, quem_somos_nos, politica_de_privacidade

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('quem_somos_nos', quem_somos_nos, name='quem_somos_nos'),
    path('politica_de_privacidade', politica_de_privacidade, name='politica_de_privacidade'),
]

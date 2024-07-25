from django.urls import path

from mercado.base.views import home, cadastro, perfil, quem_somos_nos, politica_de_privacidade, politica_de_entrega, \
    trocas_e_devolucoes, políticas_de_cancelamentos_e_ressarcimentos

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('quem_somos_nos', quem_somos_nos, name='quem_somos_nos'),
    path('politica_de_privacidade', politica_de_privacidade, name='politica_de_privacidade'),
    path('politica_de_entrega', politica_de_entrega, name='politica_de_entrega'),
    path('trocas_e_devolucoes', trocas_e_devolucoes, name='trocas_e_devolucoes'),
    path('políticas_de_cancelamentos_e_ressarcimentos', políticas_de_cancelamentos_e_ressarcimentos,
         name='políticas_de_cancelamentos_e_ressarcimentos'),
]

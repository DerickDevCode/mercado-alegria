from django.urls import path

from mercado.base.views import home, cadastro, perfil, editar_perfil

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar_perfil', editar_perfil, name='editar_perfil'),
]

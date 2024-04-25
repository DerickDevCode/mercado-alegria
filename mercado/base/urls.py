from django.urls import path

from mercado.base.views import home, cadastro_e_login

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('login', cadastro_e_login, name='cadastro_e_login'),
]

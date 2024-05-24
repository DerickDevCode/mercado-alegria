import re

from django import forms
from django.core.exceptions import ValidationError

from mercado.base.models import User
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'email', 'cpf', 'phone_number', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento: (ex: 00/00/0000)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF (ex: 000.000.000-00)'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Número de Telefone: (ex: 99 99999-9999)'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        }

    error_messages = {
        'first_name': {
            'nome_curto': _('Seu Nome precisa ter no mínimo 2 caracteres.'),
            'caracteres_invalidos': _('Os caracteres são inválidos, use apenas letras.')
        },
        'last_name': {
            'nome_curto': _('Seu Nome precisa ter no mínimo 2 caracteres.'),
            'caracteres_invalidos': _('Os caracteres são inválidos, use apenas letras.')
        },
        'cpf': {
            'cpf_invalido': _('Por favor insira um CPF válido.'),
        },
        'phone_number': {
            'numero_invalido': _('Por favor insira um número de telefone válido.'),
        },
        'password': {
            'numeros_e_letras': _('Sua senha deve conter números e letras.'),
            'senha_curta': _('Sua senha deve conter no mínimo 6 caracteres.'),
        },
    }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not ''.join(first_name.split()).isalpha():
            raise ValidationError(self.error_messages['first_name']['caracteres_invalidos'])
        if len(first_name) < 2:
            raise ValidationError(self.error_messages['first_name']['nome_curto'])
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not ''.join(last_name.split()).isalpha():
            raise ValidationError(self.error_messages['cpf']['caracteres_invalidos'])
        if len(last_name) < 2:
            raise ValidationError(self.error_messages['last_name']['nome_curto'])
        return last_name

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not ''.join(re.split('[.-]', cpf)).isnumeric():
            raise ValidationError(self.error_messages['cpf']['cpf_invalido'])
        if not len(''.join(re.split('[.-]', cpf))) == 11:
            raise ValidationError(self.error_messages['cpf']['cpf_invalido'])
        return cpf

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not ''.join(re.split('[ -]', phone_number)).isnumeric():
            raise ValidationError(self.error_messages['phone_number']['numero_invalido'])
        if not len(''.join(re.split('[ -]', phone_number))) == 11:
            raise ValidationError(self.error_messages['phone_number']['numero_invalido'])
        return phone_number

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not len(password) >= 6:
            raise ValidationError(self.error_messages['password']['senha_curta'])
        if password.isalpha() or password.isnumeric():
            raise ValidationError(self.error_messages['password']['numeros_e_letras'])
        return password

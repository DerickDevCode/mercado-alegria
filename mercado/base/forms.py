from django import forms

from mercado.base.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'email', 'cpf', 'phone_number', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Sobrenome'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control mb-4', 'placeholder': 'Data de Nascimento: (ex: 00/00/0000)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-4', 'placeholder': 'E-mail'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'CPF (ex: 000.000.000-00)'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control mb-4', 'placeholder': 'Número de Telefone: (ex: 99 99999-9999)'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Senha'}),
        }

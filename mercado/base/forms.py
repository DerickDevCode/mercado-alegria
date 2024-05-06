from django import forms

from mercado.base.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'email', 'cpf', 'phone_number')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Sobrenome'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Data de Nascimento'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-4', 'placeholder': 'E-mail'}),
            'cpf': forms.NumberInput(attrs={'class': 'form-control mb-4', 'placeholder': 'CPF'}),
            'phone_number': forms.NumberInput(
                attrs={'class': 'form-control mb-4', 'placeholder': 'Número de Telefone'}),
            # campo da senha
        }

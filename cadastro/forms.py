from django import forms
from .models import User 

class CadastroForm(forms.ModelForm):
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
        error_messages = {
            'email': {
                'unique': "Este e-mail já está cadastrado.",
            },
        }
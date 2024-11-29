from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nome','email','cpf', 'dataNascimento',  'senha','telefone','tipoUsuario','endereco','tipoDoenca',]

        widgets = {
            'dataNascimento': forms.DateInput(attrs ={'type': 'date'}),
            'senha': forms.PasswordInput(),
        }
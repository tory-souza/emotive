from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nome','email','cpf', 'dataNascimento',  'senha','telefone','endereco','tipoDoenca',]

        widgets = {
            'dataNascimento': forms.DateInput(attrs ={'type': 'date'}),
            'senha': forms.PasswordInput(),
            'telefone':forms.TextInput(attrs={'id': 'id_telefone'})
        }
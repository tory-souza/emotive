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

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("O email já está cadastrado. Tente outro.")
        return email    


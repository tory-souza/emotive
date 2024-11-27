from django.shortcuts import render, redirect
from .models import Paciente
from django.contrib import messages


def index(request):
    return render(request, 'sistema/index.html')

def acesso(request):
    return render(request, 'sistema/acesso.html')

def cadastroUser(request):
    return render(request, 'sistema/cadastroUser.html')

def consultarPac(request):
    return render(request, 'sistema/consultarPac.html')

def consultasDaSemana(request):
    return render(request, 'sistema/consultasDaSemana.html')

def dicasalimentacao(request):
    return render(request, 'sistema/dicasalimentacao.html')

def intensidade(request):
    return render(request, 'sistema/intensidade.html')

# Tela de login
def login(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        senha = request.POST['senha']
        nome = request.POST['nome']

        try:
            paciente = Paciente.objects.get(cpf=cpf, senha=senha, nome=nome)
            messages.success(request, f'Bem-vindo, {paciente.nome}!')
            return redirect('acesso')
        except Paciente.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'sistema/login.html')


def loginmedico(request):
    return render(request, 'sistema/loginmedico.html')

def menuMedico(request):
    return render(request, 'sistema/menuMedico.html')

def pacienteRisco(request):
    return render(request, 'sistema/pacienteRisco.html')

def reset(request):
    return render(request, 'sistema/reset.html')

def sonopaciente(request):
    return render(request, 'sistema/sonopaciente.html')
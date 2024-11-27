from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente
from django.contrib import messages
from .forms import MedicoForm, PacienteForm, DiarioForm, ConsultaForm

def index(request):
    return render(request, 'sistema/index.html')

def acesso(request):
    return render(request, 'sistema/acesso.html')

def cadastroUser(request):
    if request.method == 'POST':
        cpf = request.POST ['cpf']
        senha = request.POST ['senha']
        confirmar_senha = request.POST ['confirmar_senha']
        
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
        elif Paciente.objects.filter(cpf=cpf).exists():
            messages.error(request, 'o nome de usúario já está em uso.')
        else:
            Paciente.objects.create(cpf=cpf, senha=senha)
            messages.success(request, 'Cadastrado com sucesso!.')
            return redirect('login')
    return render(request, 'sistema/cadastroUser.html')

def consultarPac(request):
    return render(request, 'sistema/consultarPac.html')

def consultasDaSemana(request):
    return render(request, 'sistema/consultasDaSemana.html')

def dicasalimentacao(request):
    return render(request, 'sistema/dicasalimentacao.html')

def intensidade(request):
    return render(request, 'sistema/intensidade.html')

def login(request):
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
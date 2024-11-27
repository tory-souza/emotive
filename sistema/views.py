from django.shortcuts import render,redirect
from .models import Paciente,Medico,Consulta,Diario
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

def login(request):
    return render(request, 'sistema/login.html')

def loginmedico(request):
    if request.method=='POST':
        email=request.POST['email']
        senha=request.POST['senha']
        
        try:
            medico=Medico.objects.get(email=email,senha=senha)
            return redirect ('sistema/menuMedico.html') #OU PODE MUDAR PARA ASSIM QUE LOGAR ELE IR PRA PACIENTES EM RISCOS
        except Medico.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos.')
             
    return render(request,'sistema/loginmedico.html')


def menuMedico(request):
    return render(request, 'sistema/menuMedico.html')

def pacienteRisco(request):
    return render(request, 'sistema/pacienteRisco.html')

def reset(request):
    return render(request, 'sistema/reset.html')

def sonopaciente(request):
    return render(request, 'sistema/sonopaciente.html')
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages


def index(request):
    return render(request, 'sistema/index.html')

def acesso(request):
    userp=request.session.get('userp', None)
    userp=userp.capitalize()
    return render(request, 'sistema/acesso.html', {'userp':userp})

def cadastroUser(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            request.session['userp'] = usuario.nome 
            return redirect('acesso')

        else:
            return render(request, 'sistema/cadastroUser.html', {'form': form})
            
    else:
        form = UsuarioForm()
    return render(request, 'sistema/cadastroUser.html', {'form': form})
    
def consultarPac(request):
    return render(request, 'sistema/consultarPac.html')

def consultasDaSemana(request):
    return render(request, 'sistema/consultasDaSemana.html')

def dicasalimentacao(request):
    return render(request, 'sistema/dicasalimentacao.html')

def intensidade(request):
    userp=request.session.get('userp', None)
    return render(request, 'sistema/intensidade.html', {'userp':userp})

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        senha=request.POST['senha']

        try:
            userp=Usuario.objects.get(email=email,senha=senha) 
            request.session['userp']=userp.nome  ##ele salva o userp em uma sessao
            return redirect('acesso')
        except Usuario.DoesNotExist:
            print("Usuario não existe!")
            mensagem_erro = "Usuário ou senha inválidos."
            return render(request, 'sistema/login.html', {'mensagem_erro': mensagem_erro})
            
    return render (request,'sistema/login.html')
        
def loginmedico(request):
    return render(request, 'sistema/loginmedico.html')

def menuMedico(request):
    return render(request, 'sistema/menuMedico.html')

def pacienteRisco(request):
    return render(request, 'sistema/pacienteRisco.html')

def reset(request):
    return render(request, 'sistema/reset.html')

def termos(request):
    return render(request, 'sistema/termos.html')

def mensagemDia(request):
    userp=request.session.get('userp', None)
    userp=userp.capitalize()
    return render(request, 'sistema/mensagemDia.html', {'userp':userp})

def sonopaciente(request):
    userp=request.session.get('userp', None)
    userp=userp.capitalize()
    return render(request, 'sistema/sonopaciente.html', {'userp':userp})

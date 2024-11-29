from django.shortcuts import render,redirect
from .models import Usuario
from .forms import UsuarioForm

def index(request):
    return render(request, 'sistema/index.html')

def acesso(request):
    return render(request, 'sistema/acesso.html')

def cadastroUser(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            form.save() 
            return redirect('acesso')
            
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
from django.shortcuts import render

def alimentos(request):
    return render(request, 'dicas/alimentos.html')

def contato(request):
    return render(request, 'dicas/contato.html')

def exercicios(request):
    return render(request, 'dicas/exercicios.html')

def alogamento(request):
    return render(request, 'dicas/alogamento.html')

def index(request):
    return render(request, 'dicas/index.html')

def sobre(request):
    return render(request, 'dicas/sobre.html')

def beneficios(request):
    return render(request, 'dicas/beneficios.html')

def yoga(request):
    return render(request, 'dicas/yoga.html')

def natacao(request):
    return render(request, 'dicas/natacao.html')

def caminhada(request):
    return render(request, 'dicas/caminhada.html')

def comoUsar(request):
    return render(request, 'dicas/comoUsar.html')
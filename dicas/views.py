from django.shortcuts import render

def alimentos(request):
    return render(request, 'dicas/alimentos.html')

def contato(request):
    return render(request, 'dicas/contato.html')

def exercicios(request):
    return render(request, 'dicas/exercicios.html')

def home(request):
    return render(request, 'dicas/home.html')

def index(request):
    return render(request, 'dicas/index.html')

def sobre(request):
    return render(request, 'dicas/sobre.html')
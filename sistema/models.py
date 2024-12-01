from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    cpf = models.CharField(max_length=12)
    email = models.EmailField(max_length=100,unique=True)
    senha = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    tipoDoenca = models.CharField(max_length=200)
    endereco=models.CharField(max_length=300)
    
    

    def __str__(self):
        return self.nome
    
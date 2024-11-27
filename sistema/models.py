from django.db import models

class Medico(models.Model):
    
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=10, unique=True)  # Número do CRM do médico
    senha= models.CharField(max_length=255)
    email= models.EmailField(unique=True)


    
    def _str_(self):
        return self.nome

class Paciente(models.Model):
    # Definição do modelo Paciente
   
    tipoDoenca = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    dataNascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11, unique=True)  # CPF com 11 caracteres
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    endereco = models.TextField()
    senha = models.CharField(max_length=255)
    dataCriacao = models.DateTimeField(auto_now_add=True)



    keyPaciente=models.ForeignKey(Medico, on_delete=models.CASCADE)

    def _str_(self):
        return self.nome


class Diario(models.Model):
    dataCriacao=models.DateField(auto_now_add=True)
    statusDiario=models.CharField(max_length=100)
    statusSono=models.CharField(max_length=100)
    qntAcordou=models.IntegerField()
    localDor=models.CharField(max_length=100)
    intencidadeDor=models.CharField(max_length=100)


    keyPaciente= models.ForeignKey(Paciente, on_delete=models.CASCADE)
    keyMedico=models.ForeignKey(Medico, on_delete=models.CASCADE)


    def  _str_(self) :
        return self.nome


class Consulta(models.Model):
   
    motivoConsulta=models.CharField(max_length=100)
    statusReliado=models.CharField(max_length=50)
    dataHora=models.DateField(auto_now_add=True)
    observacao=models.TextField()
    diagnostico=models.CharField(max_length=100)
    
    keyMedico=models.ForeignKey(Medico, on_delete=models.CASCADE)
    keyPaciente= models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def  _str_(self) :
        return self.nome

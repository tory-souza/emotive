from django import forms
from .models import Medico, Paciente, Diario, Consulta

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'especialidade', 'crm', 'senha', 'email']
        
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['tipoDoenca', 'nome', 'dataNascimento', 'sexo', 'cpf', 'telefone', 'email', 'endereco', 'senha']
        
class DiarioForm(forms.Modelform):
    class Meta:
        model = Diario
        fields = ['statusDiario', 'statusSono', 'qntAcordou', 'localDor', 'intensidadeDor']
        
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['motivoConsulta', 'statusReliado', 'observacao', 'diagnostico']
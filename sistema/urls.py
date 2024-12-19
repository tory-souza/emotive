from django.urls import path
from . import views
urlpatterns = [
    path ('', views.index, name='index'),
    path ('acesso', views.acesso, name='acesso'),
    path ('cadastroUser', views.cadastroUser, name='cadastroUser'),
    path ('consultarPac', views.consultarPac, name='consultarPac'),
    path ('consultasDaSemana', views.consultasDaSemana, name='consultasDaSemana'),
    path ('dicasalimentacao', views.dicasalimentacao, name='dicasalimentacao'),
    path ('intensidade', views.intensidade, name='intensidade'),
    path ('mensagemDia', views.mensagemDia, name='mensagemDia'),
    path ('login', views.login, name='login'),
    path ('loginmedico', views.loginmedico, name='loginmedico'),
    path ('menuMedico', views.menuMedico, name='menuMedico'),
    path ('pacienteRisco', views.pacienteRisco, name='pacienteRisco'),
    path ('reset', views.reset, name='reset'),
    path ('sonopaciente', views.sonopaciente, name='sonopaciente'),
    path ('termos', views.termos, name='termos'),
]

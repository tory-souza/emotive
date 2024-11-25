from django.urls import path
from . import views
urlpatterns = [
    path ('', views.index, name='index'),
    path ('alimentos', views.alimentos, name='alimentos'),
    path ('contato', views.contato, name='contato'),
    path ('exercicios', views.exercicios, name='exercicios'),
    path ('home', views.home, name='home'),
    path ('sobre', views.sobre, name='sobre'),
]
from django.urls import path
from . import views
urlpatterns = [
    path ('', views.index, name='index'),
    path ('alimentos', views.alimentos, name='alimentos'),
    path ('alogamento', views.alogamento, name='alogamento'),
    path ('beneficios', views.beneficios, name='beneficios'),
    path ('contato', views.contato, name='contato'),
    path ('sobre', views.sobre, name='sobre'),
    path ('exercicios', views.exercicios, name='exercicios'),
    path ('yoga', views.yoga, name='yoga'),
    path ('natacao', views.natacao, name='natacao'),
    path ('caminhada', views.caminhada, name='caminhada'),
    path ('comoUsar', views.comoUsar, name='comoUsar'),
]
from django.urls import path

# Importa as views do app enquetes
from . import views

# Define o namespace do app enquetes
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questao_id>', views.detalhes, name='detalhes'),
    path('<int:questao_id>/resultados/', views.resultados, name='resultados'),
    path('<int:questao_id>/votar/', views.votar, name='votar'),
]

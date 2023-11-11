from django.urls import path

# Importa as views do app enquetes
from . import views

# Define o namespace do app enquetes
urlpatterns = [
    path('', views.index, name='index'),
]

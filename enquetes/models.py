import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Questao(models.Model):

    def __str__(self):
        return self.texto_questao

    # Cria um campo de texto com no máximo 200 caracteres.
    texto_questao = models.CharField(max_length=200)

    # Cria um campo de data e hora.
    data_publicacao = models.DateTimeField('data de publicação')

    def foi_publicado_recentemente(self):
        return self.data_publicacao >= timezone.now() - datetime.timedelta(days=1)
    
class Escolha(models.Model):

    def __str__(self):
        return self.texto_escolha
    
    # Cria uma chave estrangeira para a classe Questao. 
    # Quando a classe Questao for excluída, todas as escolhas relacionadas 
    # a ela também serão excluídas.
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)

    texto_escolha = models.CharField(max_length=200)

    # Cria um campo de número inteiro.
    votos = models.IntegerField(default=0)
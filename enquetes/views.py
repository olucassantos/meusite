from django.shortcuts import render
from django.http import HttpResponse
from .models import Questao

# Create your views here.
def index(request):
    # Carrega as 5 questões mais recentes ordenadas por data de publicação
    lista_questoes_recentes = Questao.objects.order_by('-data_publicacao')[:5]

    # Cria um dicionário com a lista de questões recentes
    context = {'lista_questoes_recentes': lista_questoes_recentes}

    # Renderiza o template index.html com o contexto
    return render(request, 'enquetes/index.html', context)

def detalhes(request, questao_id):
    return HttpResponse("Você está procurando pela questão %s" % questao_id)

def resultados(request, questao_id):
    response = "Você está procurando pelos resultados da questão %s"
    return HttpResponse(response % questao_id)

def votar(request, questao_id):
    return HttpResponse("Você está votando na questão %s" % questao_id)
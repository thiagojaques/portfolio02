from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

from portfolio.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200

def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')


def test_formulario_presente(resposta):
    assertContains(resposta, '<form')

@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa 1', feita=False),
        Tarefa(nome='Tarefa 2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas

@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes):
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_lista_de_tarefas_pendentes_presente(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefas in lista_de_tarefas_pendentes:
        assertContains(resposta_com_lista_de_tarefas, tarefas.nome)



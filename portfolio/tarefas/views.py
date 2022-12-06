from django.forms import Form
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from portfolio.tarefas.forms import TarefaForm, TarefaNovaForm
from portfolio.tarefas.models import Tarefa

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()

            return render(request, 'tarefas/home.html',
            {
                'form': form,
                'tarefas_pendentes' : tarefas_pendentes,
                'tarefas_feitas' : tarefas_feitas
            },
            status=400)
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()

    return render(request, 'tarefas/home.html',
            {   
                'Form': Form,
                'tarefas_pendentes' : tarefas_pendentes,
                'tarefas_feitas' : tarefas_feitas
            })


def detalhe(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST, instance=tarefa)
    if form.is_valid():
        form.save()

    return HttpResponseRedirect(reverse('tarefas:home'))

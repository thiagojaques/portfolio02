from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from portfolio.tarefas.forms import TarefaNovaForm
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

            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes' : tarefas_pendentes}, status= 400)
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()

    return render(request, 'tarefas/home.html', {'tarefas_pendentes' : tarefas_pendentes})
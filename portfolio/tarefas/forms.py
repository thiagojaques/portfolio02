from django.forms.models import ModelForm
from portfolio.tarefas.models import Tarefa

class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome','feita']
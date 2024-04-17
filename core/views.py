from django.shortcuts import render
from django.views.generic import ListView
from servico.models import Servico

class IndexListView(ListView):
    model = Servico
    template_name = 'index.html'
    context_object_name = 'servicos'

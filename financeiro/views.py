from django.shortcuts import render
from rest_framework import viewsets
from financeiro.models import Despesas, Receitas
from financeiro.serializers import DespesasSerializer, ReceitasSerializer
# Create your views here.


class ReceitasViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer

    
class DespesasViewSet(viewsets.ModelViewSet):
    queryset = Despesas.objects.all()
    serializer_class = DespesasSerializer
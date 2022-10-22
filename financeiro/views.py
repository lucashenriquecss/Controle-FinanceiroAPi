
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from financeiro.models import Despesas, Receitas
from financeiro.serializers import DespesasSerializer, ReceitasSerializer,ListaReceitasPorMesSerializer,ListaDespesasPorMesSerializer
from rest_framework import filters
from django.db.models import Sum

# Create your views here.
import datetime

class ReceitasViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']



class DespesasViewSet(viewsets.ModelViewSet):
    queryset = Despesas.objects.all()
    serializer_class = DespesasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']


class ListaReceitasPorMesViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Receitas.objects.filter(data__year = self.kwargs['year'] , data__month = self.kwargs['month'])
        return queryset
    serializer_class = ListaReceitasPorMesSerializer

class ListaDespesasPorMesViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Despesas.objects.filter(data__year = self.kwargs['year'] , data__month = self.kwargs['month'])
        return queryset
    serializer_class = ListaDespesasPorMesSerializer

class ResumodoMesView(APIView):
    def get(self,request,mes,ano):
        receita_mes =  Receitas.objects.filter(data__month = mes,data__year =ano).aggregate(TOTAL = Sum('valor'))['TOTAL']
        despesa_mes =  Despesas.objects.filter(data__month = mes,data__year =ano).aggregate(TOTAL = Sum('valor'))['TOTAL']
        total =  receita_mes - despesa_mes
        categoria = Despesas.objects.filter(data__month = mes, data__year = ano,).values('categoria').annotate(total = Sum('valor'))
        return Response ({
            'Receita do Mês' : f"R$ {receita_mes}",
            'Despesa do Mês' : f"R$ {despesa_mes}",
            'Saldo restante' : f"R$ {total}",
            'Gasto por categoria' : categoria,
        
        })
   
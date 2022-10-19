from django.shortcuts import render
from rest_framework import viewsets
from financeiro.models import Receitas
from financeiro.serializers import ReceitasSerializer
# Create your views here.


class ReceitasViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer

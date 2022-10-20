from rest_framework import serializers
from financeiro.models import Despesas, Receitas
# from financeiro.validators import *


class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = '__all__'
    # def validate(self,data):
    #     if not validate_descricao(data['descricao']):
    #         raise serializers.ValidationError({'descricao':"A descrição deve ter mais de 2 letras"})
    #     return data

class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = '__all__'    
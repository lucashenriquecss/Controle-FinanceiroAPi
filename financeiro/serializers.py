from rest_framework import serializers
from financeiro.models import Despesas, Receitas



class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = '__all__'

    def validate_descricao(self,descricao):
        if len(descricao) <= 2:
            raise serializers.ValidationError({'descricao':"A descrição deve ter mais de 2 letras"})
        return descricao





class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = '__all__'    
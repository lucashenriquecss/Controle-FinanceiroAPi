from rest_framework import serializers
from financeiro.models import Despesas, Receitas
import datetime


class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = '__all__'

    def validate_descricao(self,descricao):
        x = datetime.datetime.now()

        if len(descricao) <= 2:
            raise serializers.ValidationError({'descricao':"A descrição deve ter mais de 2 letras"})
        for instance in Receitas.objects.all():
            if instance.data.strftime("%B") == x.strftime("%B") and instance.descricao == descricao: 
                raise serializers.ValidationError({'data':"A descrição ja existe este mes"})
        return descricao

    
        




class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = '__all__'

    def validate_descricao(self,descricao):
        x = datetime.datetime.now()

        if len(descricao) <= 2:
            raise serializers.ValidationError({'descricao':"A descrição deve ter mais de 2 letras"})
        for instance in Despesas.objects.all():
            if instance.data.strftime("%B") == x.strftime("%B") and instance.descricao == descricao: 
                print(instance.data.strftime("%B"))
                raise serializers.ValidationError({'data':"A descrição ja existe este mes"})
        return descricao    
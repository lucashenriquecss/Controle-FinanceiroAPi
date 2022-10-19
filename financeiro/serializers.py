from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from financeiro.models import Receitas



class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = '__all__'
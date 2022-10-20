
from django.db import models
from datetime import  datetime
# Create your models here.


class Receitas(models.Model):
    descricao = models.CharField(max_length=200,blank=False)
    valor = models.IntegerField(blank=False)
    data = models.DateField(default=datetime.now, blank=False)

    def __str__(self):
        return self.descricao

class Despesas(models.Model):
    descricao = models.CharField(max_length=200,blank=False)
    valor = models.IntegerField(blank=False)
    data = models.DateField(default=datetime.now, blank=False)

    def __str__(self):
        return self.descricao  
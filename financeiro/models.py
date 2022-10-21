
from django.db import models
from datetime import  datetime
# Create your models here.


class Receitas(models.Model):
    descricao = models.CharField(max_length=200,blank=False)
    valor = models.IntegerField(blank=False)
    data = models.DateField(default=datetime.now, blank=False)

    def __str__(self):
        return self.descricao



CATEGORIA = (
    ("Outras","Outras"),
    ("Alimentação","Alimentação"),
    ("Saúde","Saúde"),
    ("Moradia","Moradia"),
    ("Transporte","Transporte"),
    ("Educação","Educação"),
    ("Lazer","Lazer"),
    ("Imprevistos","Imprevistos"),

)
class Despesas(models.Model):
    descricao = models.CharField(max_length=200,blank=False)
    valor = models.IntegerField(blank=False)
    data = models.DateField(default=datetime.now, blank=False)
    categoria = models.CharField(max_length=20,choices=CATEGORIA,default="Outras")
    def __str__(self):
        return self.descricao  



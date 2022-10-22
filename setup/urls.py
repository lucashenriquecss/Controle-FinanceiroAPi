
from typing import List
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from financeiro.views import DespesasViewSet, ListaDespesasPorMesViewSet, ReceitasViewSet,ListaReceitasPorMesViewSet,ResumodoMesView

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='receitas')
router.register('despesas', DespesasViewSet, basename='despesas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas-mes/<int:year>/<int:month>/',ListaReceitasPorMesViewSet.as_view()),
    path('despesas-mes/<int:year>/<int:month>/',ListaDespesasPorMesViewSet.as_view()),
    path('resumo/<int:ano>/<int:mes>/',ResumodoMesView.as_view()),
]

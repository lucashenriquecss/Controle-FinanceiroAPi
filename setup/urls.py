
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from financeiro.views import DespesasViewSet, ReceitasViewSet

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='receitas')
router.register('despesas', DespesasViewSet, basename='despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/', ReceitasViewSet.as_view({'get': 'list'})),
    path('despesas/', DespesasViewSet.as_view({'get': 'list'})),
]

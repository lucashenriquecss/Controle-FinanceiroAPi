
from typing import List
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from financeiro.views import DespesasViewSet,UsuarioViewSet,CriarUsuarioViewset, ListaDespesasPorMesViewSet, ReceitasViewSet,ListaReceitasPorMesViewSet,ResumodoMesView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="API Financeira",
      default_version='v1',
      description="Registro de Receitas e Despesas",
      terms_of_service="#",
      
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='receitas')
router.register('despesas', DespesasViewSet, basename='despesas')
router.register('usuarios', UsuarioViewSet, basename='usuarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('users/',CriarUsuarioViewset.as_view()),
    path('receitas-mes/<int:year>/<int:month>/',ListaReceitasPorMesViewSet.as_view()),
    path('despesas-mes/<int:year>/<int:month>/',ListaDespesasPorMesViewSet.as_view()),
    path('resumo/<int:ano>/<int:mes>/',ResumodoMesView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

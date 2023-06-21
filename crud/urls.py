from django.urls import path
from crud.api.views import PropostaViewSet, PropostaCustomFieldViewSet
from .views import PropostaRegistrer

urlpatterns = [
    # Rota para exibir o formulário de preenchimento da proposta
    path('proposta/', PropostaViewSet.as_view({'get': 'list', "post": "create"}), name='proposta'),
    path('campos/', PropostaCustomFieldViewSet.as_view({'get': 'list'}), name='campos'),
]
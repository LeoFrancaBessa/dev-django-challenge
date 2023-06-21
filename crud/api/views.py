from rest_framework import viewsets
from rest_framework import status
import json
from rest_framework.response import Response

from .utils import create_custom_fields_answers
from crud.tasks import check_propostas

from crud.models import Proposta, PropostaCustomField
from .serializers import PropostaSerializer, PropostaCustomFieldSerializer


class PropostaViewSet(viewsets.ModelViewSet):

    serializer_class = PropostaSerializer
    queryset = Proposta.objects.all()

    def create(self, request):
        #Por conta do formato que o ajax envia os dados, é preciso remaneja-los para que fiquem no padrão do drf
        data = json.loads(list(request.data.keys())[0])
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            #O serializer.data irá conter as informações das respostas dos customs_fields
            #É preciso guardar em uma variavel separada para usar na função
            custom_fields = data["custom_fields"]
            object = serializer.save()
            #Função que ira criar o objeto das respostas dos custom_fields
            create_custom_fields_answers(object, custom_fields)
            #Tarefa para analisar as propostas
            check_propostas.delay(object.id)
            response = {"Operação processada com sucesso!"}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {f"Operação não processada, erros: {serializer.errors}"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    

#View que será chamada para obter todos os campos customizados cadastrados
class PropostaCustomFieldViewSet(viewsets.ModelViewSet):
    
    serializer_class = PropostaCustomFieldSerializer
    queryset = PropostaCustomField.objects.all()
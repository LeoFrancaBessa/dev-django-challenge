from rest_framework import serializers
from crud.models import Proposta, PropostaCustomFieldAnswer, PropostaCustomField

#Serializer para retornar todas as repostas registradas na proposta
class PropostaCustomFieldAnswerSerializer(serializers.ModelSerializer):
    custom_field_title = serializers.SerializerMethodField()

    def get_custom_field_title(self, obj):
        return obj.customfield.title

    class Meta:
        model = PropostaCustomFieldAnswer
        fields = ("custom_field_title", "answer")


#Serializer para retornar todas os campos customizados cadastrados
class PropostaCustomFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropostaCustomField
        fields = ("id", "title")


#Serializer para a Proposta em si
class PropostaSerializer(serializers.ModelSerializer):
    #Este campo será utilizado para guardar as respostas dos campos customizados durante o POST
    custom_fields = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField()), required=False
    )
    custom_fields_answers = serializers.SerializerMethodField()

    def get_custom_fields_answers(self, obj):
        q = obj.answers.all()
        return PropostaCustomFieldAnswerSerializer(q, many=True).data


    def create(self, validated_data):
        #Como o campo custom_fields não faz parte do model Proposta, é preciso remove-lo do dicionário ao criar o objeto
        validated_data.pop("custom_fields")
        return super().create(validated_data)

    class Meta:
        model = Proposta
        fields = ("status", "value", "custom_fields_answers", "custom_fields")
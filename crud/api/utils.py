#Arquivo para gaurdar as funções
from crud.models import PropostaCustomFieldAnswer, PropostaCustomField

#Função para criar a resposta dos campos customizados da proposta
#O dicionário do custom_fields irá receber o ID do campo e o texto da resposta
def create_custom_fields_answers(proposta, custom_fields):
    proposta_custom_fields_answers = []
    for answer in custom_fields:
        field = PropostaCustomField.objects.filter(pk=answer['field_id']).first()
        if field:
            proposta_custom_fields_answers.append(
                PropostaCustomFieldAnswer(
                answer = answer["answer"],
                customfield = field,
                proposta = proposta,
                )
            )
    
    PropostaCustomFieldAnswer.objects.bulk_create(proposta_custom_fields_answers)
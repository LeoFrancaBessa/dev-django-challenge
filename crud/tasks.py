from celery import shared_task
import random
from crud.models import Proposta
import logging


@shared_task
def check_propostas(object_id):
    logging.debug("Inicio da tarefa")
    proposta = Proposta.objects.get(pk=object_id)
    status = str(random.randint(1, 2))
    proposta.status = status
    proposta.save()
from django.shortcuts import render
from django.views.generic import TemplateView

#View que será utilizada como página inicial
class PropostaRegistrer(TemplateView):
    template_name = "home.html"
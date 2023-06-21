from django.db import models


#Modelo para o objeto principal da proposta
class Proposta(models.Model):
    STATUS_CHOICES = (
        ("0", "Em Análise"),
        ("1", "Aprovada"),
        ("2", "Negada"),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='0')
    value = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"

    def __str__(self):
        return f"{self.get_status_display()} - R$ {str(self.value)}"


#Modelo para registrar os campos que o admin pode adicionar na proposta
class PropostaCustomField(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Campo Customizado"
        verbose_name_plural = "Campos Customizados"

    def __str__(self):
        return self.title


#Modelo para guardar os valores que o usuário preencheu nos campos customizados
class PropostaCustomFieldAnswer(models.Model):
    answer = models.CharField(max_length=500)
    customfield = models.ForeignKey(PropostaCustomField, on_delete=models.CASCADE)
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name="answers")

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"

    def __str__(self):
        return f"{self.customfield} - {self.answer}"
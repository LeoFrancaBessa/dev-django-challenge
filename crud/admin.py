from django.contrib import admin
from crud.models import Proposta, PropostaCustomField, PropostaCustomFieldAnswer

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ("id", "value", "status")
    fields = ["status", "value"]
    readonly_fields = ("status",)
    search_fields = (
        "status",
    )


@admin.register(PropostaCustomField)
class PropostaCustomFieldAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = (
        "title",
    )
    ordering = ("order",)

@admin.register(PropostaCustomFieldAnswer)
class PropostaCustomFieldAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "proposta", "customfield", "answer")
    search_fields = (
        "answer",
        "customfield",
    )

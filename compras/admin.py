from django.contrib import admin
from .models import Compra, HistoricoCompra


class HistoricoCompraInline(admin.TabularInline):
    model = HistoricoCompra
    extra = 1
    readonly_fields = ("data",)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "status",
        "prioridade",
        "solicitante",
        "fornecedor",
        "valor",
        "dias_parado",
        "data_atualizacao",
    )

    list_filter = (
        "status",
        "prioridade",
    )

    search_fields = (
        "titulo",
        "descricao",
        "solicitante",
        "fornecedor",
    )

    inlines = [HistoricoCompraInline]


@admin.register(HistoricoCompra)
class HistoricoCompraAdmin(admin.ModelAdmin):
    list_display = (
        "compra",
        "acao",
        "usuario",
        "data",
    )

    list_filter = (
        "data",
    )

    search_fields = (
        "compra__titulo",
        "acao",
        "usuario",
    )
# Register your models here.



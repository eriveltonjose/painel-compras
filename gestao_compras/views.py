from .services_wbc import buscar_compras_wbc, ETAPAS_WBC
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from .models import SolicitacaoCompra

def dashboard(request):
    compras_wbc = buscar_compras_wbc()

    kanban = {}

    for status_codigo, status_nome in ETAPAS_WBC.items():
        kanban[status_codigo] = {
            "nome": status_nome,
            "compras": []
        }

    for compra in compras_wbc:
        status = compra.get("status")

        if status in kanban:
            kanban[status]["compras"].append(compra)

    total_solicitacoes = len(compras_wbc)
    compras_abertas = len([
        c for c in compras_wbc
        if c.get("status") not in ["movimentacao_obrigacao"]
    ])
    valor_total = sum([
        c.get("valor", 0) or 0
        for c in compras_wbc
    ])

    return render(request, "gestao_compras/dashboard.html", {
        "kanban": kanban,
        "total_solicitacoes": total_solicitacoes,
        "compras_abertas": compras_abertas,
        "valor_total": valor_total,
    })

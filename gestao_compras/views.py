from django.shortcuts import render
from compras.models import Compra
from .services_wbc import ETAPAS_WBC


def dashboard(request):
    compras_wbc = Compra.objects.all()

    kanban = {}

    for status_codigo, status_nome in ETAPAS_WBC.items():
        kanban[status_codigo] = {
            "nome": status_nome,
            "compras": []
        }

    for compra in compras_wbc:
        status = compra.status

        if status in kanban:
            kanban[status]["compras"].append(compra)

    total_solicitacoes = compras_wbc.count()

    compras_abertas = compras_wbc.exclude(
        status__in=["pago", "cancelado"]
    ).count()

    valor_total = sum([
        compra.valor or 0
        for compra in compras_wbc
    ])

    compras_urgentes = compras_wbc.filter(
        prioridade="Urgente"
    ).count()

    processos_criticos = compras_wbc.filter(
        dias_parado__gt=5
    ).count()

    aguardando_diretoria = compras_wbc.filter(
        status__in=[
            "aguardando_liberacao",
            "aguardando_aprovacao_final",
            "pagamento_liberado"
        ]
    ).count()

    aguardando_pagamento = compras_wbc.filter(
        status="aguardando_pagamento"
    ).count()

    total_adiantamento = compras_wbc.filter(
        status="adiantamento_fornecedor"
        ).count()
    
    return render(request, "gestao_compras/dashboard.html", {
        "compras_urgentes": compras_urgentes,
        "processos_criticos": processos_criticos,
        "aguardando_diretoria": aguardando_diretoria,
        "aguardando_pagamento": aguardando_pagamento,
        "kanban": kanban,
        "total_solicitacoes": total_solicitacoes,
        "compras_abertas": compras_abertas,
        "valor_total": valor_total,
        "total_adiantamento": total_adiantamento,
    })
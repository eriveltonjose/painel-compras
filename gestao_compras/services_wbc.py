# gestao_compras/services_wbc.py

def buscar_compras_wbc():
    """
    Função provisória.
    Depois vamos substituir isso pela API ou banco do WBC.
    """

    compras = [
    {
        "id": 1,
        "titulo": "Compra de Material de Escritório",
        "descricao": "Aquisição de papel A4 e toners",
        "valor": 3200,
        "status": "em_cotacao",
        "solicitante": "Carlos Silva",
        "fornecedor": "Papelaria Brasil",
        "prioridade": "Normal",
        "dias_parado": 2,
    },

    {
        "id": 2,
        "titulo": "Compra de Equipamentos TI",
        "descricao": "Notebooks para equipe administrativa",
        "valor": 18500,
        "status": "aguardando_aprovacao_final",
        "solicitante": "Fernanda Lima",
        "fornecedor": "Dell",
        "prioridade": "Urgente",
        "dias_parado": 5,
    },

    {
        "id": 3,
        "titulo": "Serviço de Manutenção",
        "descricao": "Manutenção preventiva do datacenter",
        "valor": 7200,
        "status": "aguardando_pagamento",
        "solicitante": "Roberto Alves",
        "fornecedor": "Tech Solutions",
        "prioridade": "Alta",
        "dias_parado": 1,
    },

    {
        "id": 4,
        "titulo": "Compra de Ar Condicionado",
        "descricao": "Instalação de novos equipamentos",
        "valor": 24000,
       # "status": "pedido_tr",
        "status": "aguardando_nota",
        "solicitante": "Juliana Costa",
        "fornecedor": "Clima Frio",
        "prioridade": "Urgente",
        "dias_parado": 8,
        "historico": [
        {
            "data": "09/05/2026 09:10",
            "acao": "Solicitação criada",
            "usuario": "Juliana Costa",
        },
        {
            "data": "09/05/2026 10:30",
            "acao": "Solicitação liberada pela diretoria",
            "usuario": "Diretoria",
        },
        {
            "data": "09/05/2026 14:00",
            "acao": "Pedido/TR gerado",
            "usuario": "Suprimentos",
        },
        {
            "data": "09/05/2026 15:20",
            "acao": "Status alterado para Aguardando Nota Fiscal",
            "usuario": "Sistema WBC",
        },
        ],
    },
]

    return compras


ETAPAS_WBC = {
    "solicitada": "Solicitada",
    "aguardando_liberacao": "Aguardando Liberação",
    "em_cotacao": "Em Cotação",
    "cotacao_encerrada": "Cotação Encerrada",
    "aguardando_aprovacao_final": "Aguardando Aprovação Final",
    "pedido_tr": "Pedido / TR",
    "adiantamento_fornecedor": "Adiantamento ao Fornecedor",
    "aguardando_nota": "Aguardando Nota Fiscal",
    "nota_lancada": "Nota Lançada",
    "aguardando_pagamento": "Aguardando Pagamento",
    "pagamento_liberado": "Pagamento Liberado",
    "pago": "Pago",
    "cancelado": "Cancelado",
}
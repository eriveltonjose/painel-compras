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
        "status": "pedido_tr",
        "solicitante": "Juliana Costa",
        "fornecedor": "Clima Frio",
        "prioridade": "Urgente",
        "dias_parado": 8,
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
    "aguardando_nota": "Aguardando Nota Fiscal",
    "nota_lancada": "Nota Lançada",
    "aguardando_pagamento": "Aguardando Pagamento",
    "pagamento_liberado": "Pagamento Liberado",
    "pago": "Pago",
    "cancelado": "Cancelado",
}
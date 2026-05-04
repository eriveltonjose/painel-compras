# gestao_compras/services_wbc.py

def buscar_compras_wbc():
    """
    Função provisória.
    Depois vamos substituir isso pela API ou banco do WBC.
    """

    compras = [
        {
            "id": 1,
            "titulo": "Compra teste WBC",
            "descricao": "Processo aguardando integração com WBC Sistemas",
            "valor": 0,
            "status": "solicitacao_compras",
        }
    ]

    return compras


ETAPAS_WBC = {
    "solicitacao_compras": "Solicitação de compras",
    "liberacao_compras": "Liberação de compras",
    "inicio_cotacao": "Início de cotação",
    "cotacao_finalizada": "Cotação finalizada",
    "liberacao_solicitacao_compras": "Liberação de solicitação de compras",
    "montar_pedido_compras": "Montar pedido de compras",
    "movimentacao_notas": "Movimentação de notas de Produtos/Serviço",
    "movimentacao_obrigacao": "Movimentação de obrigação",
}
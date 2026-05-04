from django.db import models
from django.contrib.auth.models import User


class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class SolicitacaoCompra(models.Model):
    STATUS_CHOICES = [
        ('solicitado', 'Solicitado'),
        ('em_aprovacao', 'Em aprovação'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
        ('em_cotacao', 'Em cotação'),
        ('pedido_emitido', 'Pedido emitido'),
        ('aguardando_entrega', 'Aguardando entrega'),
        ('recebido', 'Recebido'),
        ('pago', 'Pago'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]

    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    solicitante = models.ForeignKey(User, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='solicitado')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    valor_estimado = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.titulo


class ItemSolicitacao(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoCompra, on_delete=models.CASCADE, related_name='itens')
    nome_item = models.CharField(max_length=150)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario_estimado = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.nome_item


class Cotacao(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoCompra, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)
    escolhida = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.fornecedor} - R$ {self.valor_total}'


class PedidoCompra(models.Model):
    solicitacao = models.OneToOneField(SolicitacaoCompra, on_delete=models.PROTECT)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    numero_pedido = models.CharField(max_length=50, unique=True)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.numero_pedido


class Recebimento(models.Model):
    pedido = models.OneToOneField(PedidoCompra, on_delete=models.PROTECT)
    recebido_por = models.ForeignKey(User, on_delete=models.PROTECT)
    data_recebimento = models.DateTimeField(auto_now_add=True)
    conferido = models.BooleanField(default=False)


class Pagamento(models.Model):
    pedido = models.OneToOneField(PedidoCompra, on_delete=models.PROTECT)
    valor_pago = models.DecimalField(max_digits=12, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(blank=True, null=True)
    pago = models.BooleanField(default=False)


class HistoricoStatus(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoCompra, on_delete=models.CASCADE)
    status_anterior = models.CharField(max_length=30, blank=True, null=True)
    status_novo = models.CharField(max_length=30)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data_alteracao = models.DateTimeField(auto_now_add=True)
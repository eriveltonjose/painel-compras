from django.db import models
class Compra(models.Model):
    PRIORIDADES = [
        ("Normal", "Normal"),
        ("Alta", "Alta"),
        ("Urgente", "Urgente"),
    ]

    STATUS = [
        ("solicitada", "Solicitada"),
        ("aguardando_liberacao", "Aguardando Liberação"),
        ("em_cotacao", "Em Cotação"),
        ("cotacao_encerrada", "Cotação Encerrada"),
        ("aguardando_aprovacao_final", "Aguardando Aprovação Final"),
        ("pedido_tr", "Pedido / TR"),
        ("aguardando_nota", "Aguardando Nota Fiscal"),
        ("nota_lancada", "Nota Lançada"),
        ("aguardando_pagamento", "Aguardando Pagamento"),
        ("pagamento_liberado", "Pagamento Liberado"),
        ("pago", "Pago"),
        ("cancelado", "Cancelado"),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(max_length=50, choices=STATUS, default="solicitada")
    prioridade = models.CharField(max_length=20, choices=PRIORIDADES, default="Normal")

    solicitante = models.CharField(max_length=150, blank=True)
    fornecedor = models.CharField(max_length=150, blank=True)

    dias_parado = models.IntegerField(default=0)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        criando = self.pk is None

        status_antigo = None
        prioridade_antiga = None

        if not criando:
            compra_antiga = Compra.objects.get(pk=self.pk)
            status_antigo = compra_antiga.status
            prioridade_antiga = compra_antiga.prioridade

        super().save(*args, **kwargs)

        if criando:
            HistoricoCompra.objects.create(
                compra=self,
                acao=f"Compra criada com status {self.get_status_display()}",
                usuario="Sistema",
            )
        else:
            if status_antigo != self.status:
                HistoricoCompra.objects.create(
                    compra=self,
                    acao=f"Status alterado de {dict(self.STATUS).get(status_antigo)} para {self.get_status_display()}",
                    usuario="Sistema",
                )

            if prioridade_antiga != self.prioridade:
                HistoricoCompra.objects.create(
                    compra=self,
                    acao=f"Prioridade alterada de {prioridade_antiga} para {self.prioridade}",
                    usuario="Sistema",
                )


class HistoricoCompra(models.Model):
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name="historicos"
    )

    data = models.DateTimeField(auto_now_add=True)
    acao = models.CharField(max_length=255)
    usuario = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.compra.titulo} - {self.acao}"    

# Create your models here.

from django.contrib import admin
from django.contrib import admin
from .models import *

admin.site.register(Departamento)
admin.site.register(Fornecedor)
admin.site.register(SolicitacaoCompra)
admin.site.register(ItemSolicitacao)
admin.site.register(Cotacao)
admin.site.register(PedidoCompra)
admin.site.register(Recebimento)
admin.site.register(Pagamento)
admin.site.register(HistoricoStatus)
# Register your models here.

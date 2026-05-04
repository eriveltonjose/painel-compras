from django.contrib import admin
from django.urls import path
from gestao_compras.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    # path('mudar-status/<int:compra_id>/<str:novo_status>/', mudar_status, name='mudar_status'),
]
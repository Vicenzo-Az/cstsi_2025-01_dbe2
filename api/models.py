# api/models.py
from django.conf import settings
from django.db import models


class DataSource(models.Model):
    SOURCE_TYPES = [
        ('CSV', 'Arquivo CSV'),
        ('API', 'API Externa'),
        ('DB', 'Banco de Dados'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    source_type = models.CharField(max_length=3, choices=SOURCE_TYPES)
    # Ex: { "url": "...", "api_key": "..." }
    connection_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class Dashboard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    config = models.JSONField()  # Configuração dos gráficos/filtros
    data_sources = models.ManyToManyField(DataSource)
    created_at = models.DateTimeField(auto_now_add=True)


class AnalysisReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    generated_by_ai = models.BooleanField(
        default=False)  # Se o relatório foi gerado por IA
    data_sources = models.ManyToManyField(DataSource)
    created_at = models.DateTimeField(auto_now_add=True)

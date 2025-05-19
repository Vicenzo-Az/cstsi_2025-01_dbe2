from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import viewsets
from .models import DataSource, Dashboard, AnalysisReport
from .serializers import DataSourceSerializer, DashboardSerializer, AnalysisReportSerializer
from rest_framework.permissions import IsAuthenticated


class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra apenas os dados do usuário logado
        return self.queryset.filter(user=self.request.user)


class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AnalysisReportViewSet(viewsets.ModelViewSet):
    queryset = AnalysisReport.objects.all()
    serializer_class = AnalysisReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

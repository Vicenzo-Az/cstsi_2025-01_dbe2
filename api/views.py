# api/views.py
from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import DataSource, Dashboard, AnalysisReport
from .serializers import DataSourceSerializer, DashboardSerializer, AnalysisReportSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


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


class CurrentUserView(generics.RetrieveUpdateAPIView):
    """
    GET: retorna os dados do usuário autenticado
    PUT/PATCH: atualiza os campos permitidos do usuário
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # sempre opera sobre o self.request.user
        return self.request.user

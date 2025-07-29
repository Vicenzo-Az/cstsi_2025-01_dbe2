# api/views.py
from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import DataSource, Dashboard, AnalysisReport, Documento
from .serializers import (
    DataSourceSerializer,
    DashboardSerializer,
    AnalysisReportSerializer,
    UserSerializer,
    SignupSerializer,
    ChangePasswordSerializer,
    DocumentoSerializer
)
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Define o usuário logado


class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Garante que o owner (user) seja sempre o usuário logado
        serializer.save(user=self.request.user)


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


class SignupView(generics.CreateAPIView):
    """
    POST /api/v1/auth/signup/
    Cria um novo usuário.
    """
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]


class ChangePasswordView(generics.UpdateAPIView):
    """
    PUT /api/v1/auth/password/change/
    Atualiza a senha do usuário logado.
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # retorna o próprio usuário
        return self.request.user


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        # mostra só os documentos do usuário
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # associa o usuário logado
        serializer.save(user=self.request.user)

# api/serializers.py
from rest_framework import serializers
from .models import DataSource, Dashboard, AnalysisReport
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = ['id', 'name', 'source_type', 'connection_details']

    def validate_source_type(self, value):
        if value not in dict(DataSource.SOURCE_TYPES).keys():
            raise serializers.ValidationError("Tipo de fonte inválido.")
        return value


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ['id', 'name', 'description', 'config', 'data_sources']

    def validate_config(self, value):
        # Valide se o JSON de configuração está no formato correto
        if 'charts' not in value:
            raise serializers.ValidationError(
                "Configuração inválida: falta 'charts'.")
        return value


class AnalysisReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisReport
        fields = ['id', 'title', 'content', 'generated_by_ai', 'data_sources']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # inclua aqui todos os campos que queira expor
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'read_only': True},
        }


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True},
        }

    def create(self, validated_data):
        # usa create_user para aplicar hashing na senha
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Senha antiga incorreta.")
        return value

    def update(self, instance, validated_data):
        # usa set_password para aplicar hashing
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance

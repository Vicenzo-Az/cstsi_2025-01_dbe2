# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DataSourceViewSet,
    DashboardViewSet,
    AnalysisReportViewSet,
    CurrentUserView,
    SignupView,
    ChangePasswordView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


router = DefaultRouter()
router.register(r'data-sources', DataSourceViewSet)
router.register(r'dashboards', DashboardViewSet)
router.register(r'analysis-reports', AnalysisReportViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/user/', CurrentUserView.as_view(), name='current_user'),
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/password/change/',
         ChangePasswordView.as_view(), name='password_change'),


    # Swagger UI endpoints
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('docs/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

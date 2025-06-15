# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataSourceViewSet, DashboardViewSet, AnalysisReportViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'data-sources', DataSourceViewSet)
router.register(r'dashboards', DashboardViewSet)
router.register(r'analysis-reports', AnalysisReportViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

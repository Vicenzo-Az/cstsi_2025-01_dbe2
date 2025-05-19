# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataSourceViewSet, DashboardViewSet, AnalysisReportViewSet

router = DefaultRouter()
router.register(r'data-sources', DataSourceViewSet)
router.register(r'dashboards', DashboardViewSet)
router.register(r'analysis-reports', AnalysisReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

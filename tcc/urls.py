from django.urls import path
from . import views as views

app_name = 'tcc'

urlpatterns = [
    path('', views.home, name='home'),
]

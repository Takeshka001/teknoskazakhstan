from django.urls import path
from . import views

urlpatterns = [
    path('ral-chart/', views.ral_chart, name='ral_chart'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ral-chart/', views.ral_chart, name='ral_chart'),
]
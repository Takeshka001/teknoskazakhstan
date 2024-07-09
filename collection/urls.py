# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.collections_list, name='collections'),
    path('collections/<str:url_name>/', views.collection_detail, name='collection_detail'),
    path('color/<str:color_id>/<str:url_name>', views.detail_color, name='detail_color'),
]
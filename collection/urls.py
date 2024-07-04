from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('collections/', views.collection_view, name='collection'),
    path('collections/<str:collection_name>/', views.collection_detail_view, name='collection_detail'),
    path('', include('mainapp.urls')),
]
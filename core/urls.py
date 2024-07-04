from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('promotions/', views.promotions, name='promotions'),
    path('collections/', views.collections, name='collections'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('favorites/', views.favorites, name='favorites'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('admin/', admin.site.urls),
]
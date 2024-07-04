from django.shortcuts import render

def ral_chart(request):
    return render(request, 'ral_chart.html')

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def promotions(request):
    return render(request, 'promotions.html')

def collections(request):
    return render(request, 'collections.html')

def catalog(request):
    return render(request, 'catalog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def favorites(request):
    return render(request, 'favorites.html')

def account(request):
    return render(request, 'account.html')

def cart(request):
    return render(request, 'cart.html')
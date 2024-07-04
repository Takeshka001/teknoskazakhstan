from django.shortcuts import render
from .models import ColorCollection

def collection_view(request):
    collections = ColorCollection.objects.values('collection_name').distinct()
    context = {'collections': collections}
    return render(request, 'collection.html', context)

def collection_detail_view(request, collection_name):
    colors = ColorCollection.objects.filter(collection_name=collection_name)
    context = {'colors': colors, 'collection_name': collection_name}
    return render(request, 'collection_detail.html', context)
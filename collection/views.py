from django.shortcuts import render, redirect
from .models import ColorsNcs, ColorsPantone, ColorsRalClassic, ColorsRalDesign, ColorsRalEffect

def collections_list(request):
    collections = [
        {"name": "Colors NCS", "url_name": "colors_ncs"},
        {"name": "Colors Pantone", "url_name": "colors_pantone"},
        {"name": "Colors Ral Classic", "url_name": "colors_ral_classic"},
        {"name": "Colors Ral Design", "url_name": "colors_ral_design"},
        {"name": "Colors Ral Effect", "url_name": "colors_ral_effect"},
    ]

    return render(request, 'collections.html', {'collections': collections})

def collection_detail(request, url_name):
    colors = {
        'colors_ncs': ColorsNcs,
        'colors_pantone': ColorsPantone,
        'colors_ral_classic': ColorsRalClassic,
        'colors_ral_design': ColorsRalDesign,
        'colors_ral_effect': ColorsRalEffect
    }
    if url_name in colors:
        items = colors[url_name].objects.all()

        # Добавление type для каждого элемента
        for item in items:
            item.type = url_name

        context = {
            'items': items,
            'url_name':url_name
        }
        return render(request, 'collection_detail.html', context)
    
    else:
        return redirect('collections')

def detail_color(request, color_id, url_name):
    colors = {
        'colors_ncs': ColorsNcs,
        'colors_pantone': ColorsPantone,
        'colors_ral_classic': ColorsRalClassic,
        'colors_ral_design': ColorsRalDesign,
        'colors_ral_effect': ColorsRalEffect
    }
    if url_name in colors:
        color = colors[url_name].objects.get(id=color_id)
        context = {
            'color': color,
        }
        return render(request, 'color_detail.html', context=context)
    return redirect('collections')
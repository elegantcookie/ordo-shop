from django.shortcuts import render
from .models import Category, Product, Promotion


def index(request):
    promos = Promotion.objects.all()
    context = {
        'promos': promos,
    }
    return render(request, 'base.html', context=context)


from django.shortcuts import render
from products.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'Store',
    }  # content
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'Store - catalog',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)

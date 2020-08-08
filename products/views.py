from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_info(request, id):
    products = get_object_or_404(Product, pk=id)
    return render(request, "productsinfo.html", {"product": products})
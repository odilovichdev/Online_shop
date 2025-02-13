from django.shortcuts import render
from .models import Category, Product


def store_view(request):
    query = request.GET.get("q")
    category = request.GET.get("category", None)
    all_ctg = Category.objects.all()
    products = Product.objects.all()
    if category:
        products = Product.objects.filter(product_ctg__name=category)
    if query:
        products = Product.objects.filter(title__icontains=query)


    data = {
        'all_ctg': all_ctg,
        "products": products
        }
    return render(request, 'store/store.html', data)


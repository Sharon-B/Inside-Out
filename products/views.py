from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    """
    A view to show all products, search products and filter by category
    """
    products = Product.objects.all()

    search_query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            search_query = request.GET['q']
            if not search_query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse('products'))

            search_queries = Q(name__icontains=search_query) | Q(
                               description__icontains=search_query)
            products = products.filter(search_queries)

    context = {
        'products': products,
        'search_term': search_query,
        'current_categories': categories,
      }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)

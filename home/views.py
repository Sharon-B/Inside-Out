from django.shortcuts import render
from products.models import Product


# Create your views here.
def index(request):
    """ A view to return the index page """
    new_arrivals = Product.objects.filter(category__name='new_arrivals')[:4]

    template = 'home/index.html'

    context = {
        'new_arrivals': new_arrivals,
    }

    return render(request, template, context)

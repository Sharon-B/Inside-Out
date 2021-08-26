from django.shortcuts import render
from products.models import Product
from blog.models import BlogPost


# Create your views here.
def index(request):
    """ A view to return the index page """

    new_arrivals = Product.objects.filter(category__name='new_arrivals')[:4]
    blog_posts = BlogPost.objects.all()[:1]

    template = 'home/index.html'

    context = {
        'new_arrivals': new_arrivals,
        'blog_posts': blog_posts,
    }

    return render(request, template, context)

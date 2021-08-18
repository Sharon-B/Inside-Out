from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """
    A view to show all products, search, filter and sort products.
    """
    products = Product.objects.all()

    search_query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search_query,
        'current_categories': categories,
        'current_sorting': current_sorting,
      }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


# Product Admin:
# Add Product
@login_required
def add_product(request):
    """
    Allow an admin user to add a product to the store
    """
    if request.user.is_superuser:

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Product added successfully!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Please check the form for errors. Product failed to add.')
        else:
            form = ProductForm()

    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'products/add_product.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit Product
@login_required
def edit_product(request, product_id):
    """
    Allow an admin user to edit a product to the store
    """
    if request.user.is_superuser:

        product = get_object_or_404(Product, pk=product_id)

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product updated successfully!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Please check the form for errors. Product failed to update.')
        else:
            form = ProductForm(instance=product)
            messages.info(request, f'Editing {product.name}')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'products/edit_product.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Delete Product
@login_required
def delete_product(request, product_id):
    """
    Allow an admin user to delete a product from the store
    """
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(request, 'Product deleted!')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    return redirect(reverse('products'))

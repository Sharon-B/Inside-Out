from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from products.models import Product
from django.contrib import messages


# View Cart
def view_cart(request):
    """
    A view to return the shopping cart contents page
    """

    template = 'cart/cart.html'

    context = {
        'on_cart_page': True,
    }

    return render(request, template, context)


# Add to Cart
def add_to_cart(request, item_id):
    """
    Add a product to the shopping cart
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request,
                         f'Successfully updated quantity \
                             of {product.name} to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request,
                         f'Successfully added {product.name} to your cart!')

    request.session['cart'] = cart

    return redirect(redirect_url)


# Adjust cart view
def adjust_cart(request, item_id):
    """
    Adjust the quantity of a product in the shopping cart
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request,
                         f'Successfully updated quantity \
                              of {product.name} to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request,
                         f'Successfully removed {product.name} from \
                             your cart!')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


# Remove from cart
def remove_from_cart(request, item_id):
    """
    Remove a product from the shopping cart
    """

    product = get_object_or_404(Product, pk=item_id)
    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request,
                         f'Successfully removed {product.name} from \
                             your cart!')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

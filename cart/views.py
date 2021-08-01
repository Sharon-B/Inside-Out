from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product
from django.contrib import messages


# Create your views here.
# View Cart
def view_cart(request):
    """ A view to return the shopping cart contents page """
    return render(request, 'cart/cart.html')


# Add to Cart
def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.warning(request,
                         f'Successfully added {product.name} to your cart!')

    request.session['cart'] = cart
    # print(request.session['cart'])          # Check cart contents
    return redirect(redirect_url)


# Adjust cart view
def adjust_cart(request, item_id):
    """ Adjust the quantity of a product in the shopping cart """

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


# Remove from cart
def remove_from_cart(request, item_id):
    """ Remove a product from the shopping cart """
    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

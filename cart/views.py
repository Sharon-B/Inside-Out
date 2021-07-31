from django.shortcuts import render, redirect


# Create your views here.
# View Cart
def view_cart(request):
    """ A view to return the shopping cart contents page """
    return render(request, 'cart/cart.html')


# Add to Cart
def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])          # Check cart contents
    return redirect(redirect_url)

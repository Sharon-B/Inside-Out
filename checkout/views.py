from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm


# Create your views here.
# Checkout view
def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

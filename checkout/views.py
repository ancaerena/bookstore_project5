from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NXuAKCssaSqNdf8JWCokRhB9VzCRQyXVoW16DLHB6wvcEJZpSf4gIBAUuyVPOyRIXyH5byISOnN1k7EDcE56eom00pHR7Mgw2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
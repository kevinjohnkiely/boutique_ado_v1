from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LX4zODAMQP2OTL4ScGSGU2wRlx0xraGmsDEoPCX3dszn1ba5m7jflLONqMmM9O5DHBaiWsRbG6h3xKJUxcbxIki00MIJX557i',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

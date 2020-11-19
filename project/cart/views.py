"""from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, 'Удалено')
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})"""
from django.contrib import messages
from cart.cart import Cart
from shop.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CartAddProductForm, Quantity
from django.http import HttpResponse


def test(response):
    for i in response.cookies:
        print('<h2>{}</h2>'.format(i))


# Rewrite using CBV

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect(to='cart:cart_detail')


def add_quantity(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect(to='cart:cart_detail')


def take_quantity(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.take(product)
    return redirect(to='cart:cart_detail')


def remove_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    return render(request, 'cart_detail.html', context={'cart': Cart(request)})


def order_redirect(request):
    return redirect('order:make_order')

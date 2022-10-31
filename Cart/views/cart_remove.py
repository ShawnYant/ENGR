from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Store.models.Product import Product
from Cart.cart import Cart
from Cart.forms import CartAddProductForm


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')



from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Store.models.Product import Product
from Cart.cart import Cart
from Cart.forms import CartAddProductForm
# import json


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    print("cart created")
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    # json_str = json.dumps(cart_add())
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')




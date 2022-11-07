from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Store.models.Product import Product
from Cart.cart import Cart
from Cart.forms import CartAddProductForm
from Customer.cuss import Cuss


def cart_detail(request):
    print("step1")
    cart = Cart(request)
    print("step2")
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
    #                                                                'override': True})
    return render(request, 'templates/web/Cart/detail.html', {'cart': cart,'cus':Cuss.cuss_id})

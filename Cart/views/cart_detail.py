import json

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from Cart.cart import Cart
from Cart.forms import CartAddProductForm
from Customer.cuss import Cuss
from Store.models.Product import Product


def cart_detail(request):
    print("step1")
    cart = Cart(request)
    print("step2")
    update = None
    
    for item in cart:
        # item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
        #                                                            'override': True})
        update=CartAddProductForm(initial={'quantity': item['quantity'],
                                                    'override': True})                                          
    return render(request, 'templates/web/Cart/detail.html', {'cart':cart, 'up':update, 'cus':Cuss.cuss_id})

from django.shortcuts import get_object_or_404, render
from Store.models.Category import Category
from Store.models.Product import Product
from Store.models.Restaurant import Restaurant
from Cart.forms import CartAddProductForm
from Customer.cuss import Cuss
from django.urls import reverse
# Create your views here.
def restaurat_detail(request, id, slug):
    restaurant = get_object_or_404(Restaurant,
                                slug=slug,
                                id=id,
                                )
    product = Product.objects.filter(restaurant_id=id) 
    cart_product_form = CartAddProductForm() 
                        
    return render(request,
                  'templates/web/Store/product/restaurant.html',
                  {'restaurant': restaurant,
                   'product': product,
                   'cart_product_form': cart_product_form,
                   'cus':Cuss.cuss_id})
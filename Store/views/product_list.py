from django.shortcuts import get_object_or_404, render
from Store.models.Category import Category
from Store.models.Product import Product
from Store.models.Restaurant import Restaurant
from Cart.forms import CartAddProductForm
# Create your views here.
def product_list(request, restaurant_slug=None):
    restaurant = None
    restaurants = Restaurant.objects.all()
    products = Product.objects.filter(available=True)
    if restaurant_slug:
        restaurant = get_object_or_404(Restaurant, 
                                     slug=restaurant_slug)
        products = products.filter(restaurant=restaurant)
    return render(request,
                  'templates\web\Store\product\list.html',
                  {'restaurant': restaurant,
                   'restaurants': restaurants,
                   'products': products})
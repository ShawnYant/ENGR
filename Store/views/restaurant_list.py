from django.shortcuts import get_object_or_404, render
from Store.models.Category import Category
from Store.models.Product import Product
from Store.models.Restaurant import Restaurant
from Cart.forms import CartAddProductForm



def restaurant_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    if category_slug:
        category = get_object_or_404(Category, 
                                     slug=category_slug)
        restaurants = restaurants.filter(category=category)
    return render(request,
                  'templates/web/Store/product/restaurant.html',
                  {'category': category,
                   'categories': categories,
                   'restaurants': restaurants})
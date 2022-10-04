from django.shortcuts import get_object_or_404, render
from .models import Category, Product, Restaurant
from Cart.forms import CartAddProductForm
# Create your views here.

def restaurant_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    restaurants = Restaurant.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, 
                                     slug=category_slug)
        restaurants = restaurants.filter(category=category)
    return render(request,
                  'templates/web/Store/product/restaurant.html',
                  {'category': category,
                   'categories': categories,
                   'restaurants': restaurants})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, 
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'templates\web\Store\product\list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()                               
    return render(request,
                  'templates\web\Store\product\detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
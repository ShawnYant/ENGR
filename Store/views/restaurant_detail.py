from django.shortcuts import get_object_or_404, render
from Store.models.Category import Category
from Store.models.Product import Product
from Store.models.Restaurant import Restaurant
from Cart.forms import CartAddProductForm
from Customer.cuss import Cuss
# Create your views here.
def restaurat_detail(request, id, slug):
    restaurant = get_object_or_404(Restaurant,
                                id=id,
                                slug=slug)
                            
    return render(request,
                  'templates/web/Store/product/detail_R.html',
                  {'restaurant': restaurant,
                   'cus':Cuss.cuss_id})
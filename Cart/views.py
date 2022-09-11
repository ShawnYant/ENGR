
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Store.models import Product
from .models import Cart
from .forms import CartAddProductForm

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'templates/web/cart/detail.html', {'cart': cart})



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')












# def search(request):
#     keyword = request.POST['searchWords']
#     list = models.Product.filter(Q(name__icontains=models.Product.category) | Q(desc__icontains=models.Product.slug))
#     SearchResult = []
#     for x in allArticle: 
#         if keyword in x.blog_title:
#             SearchResult.append(x)
#         elif keyword in x.blog_body:
#             SearchResult.append(x)
#     SearchStatus = "Error" if len(SearchResult) == 0 else "Success"
#     ResultAmount = len(SearchResult)

#     return render(request, 'blog/search.html', {"keyword": keyword,
#                                                 "SearchResult": SearchResult,
#                                                 "SearchStatus": SearchStatus,
#                                                 "ResultAmount": ResultAmount})
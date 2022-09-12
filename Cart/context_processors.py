
from Cart.models import Cart
def cart(request):
    return {'cart': Cart(request)}
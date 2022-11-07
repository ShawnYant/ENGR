from django.urls import reverse
from django.shortcuts import render,redirect
from Customer.models.customer import Customer
from Order.tasks import order_created

# Create your views here.
from Order.models.OrderItem import OrderItem
from Order.forms import OrderCreateForm
from Cart.cart import Cart
# from Customer.cuss import Cuss
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product_id=item['id'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
             # launch asynchronous task
            order_created.delay(order.id)
            return render(request,
                        'templates/web/Order/created.html',
                        {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                'templates/web/Order/create.html',
                {'cart': cart, 'form': form})
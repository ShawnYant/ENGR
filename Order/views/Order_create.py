from django.urls import reverse
from django.shortcuts import render,redirect
from Customer.cuss import Cuss
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
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request,
                'templates/web/Order/create.html',
                {'cart': cart, 'form': form})
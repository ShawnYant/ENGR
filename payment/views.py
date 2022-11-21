from decimal import Decimal
import stripe
from ENGR import settings
from django.shortcuts import render, redirect,\
                             get_object_or_404
from Order.models import Order
from django.urls import  reverse
from Customer.cuss import Cuss

# create the Stripe instance

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(
                        reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(
                        reverse('payment:canceled'))
        # Stripe checkout session data
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        # add order items to the Stripe checkout session
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            })
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        # redirect to Stripe payment form
        return redirect(session.url, code=303)
    else:
        return render(request, 'templates/web/payment/process.html',locals())


def payment_completed(request):
    cus=Cuss.cuss_id
    return render(request, 'templates/web/payment/completed.html',{'cus':cus})
def payment_canceled(request):
    cus=Cuss.cuss_id
    return render(request, 'templates/web/payment/canceled.html',{'cus':cus})
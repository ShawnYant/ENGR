from django.urls import path
from Order.views import Order_create
app_name = 'orders'

urlpatterns = [
    path('create/', Order_create.order_create, name='order_create'),
]
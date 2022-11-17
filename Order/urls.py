from django.urls import path
from Order.views import Order_create,Order_show
app_name = 'orders'

urlpatterns = [
    path('create/', Order_create.order_create, name='order_create'),
    path('order/', Order_show.order_show, name='order_show'),

]
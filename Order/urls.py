from django.urls import path
from Order.views import order_create, order_show
app_name = 'orders'

urlpatterns = [
    path('create/', order_create.order_create, name='order_create'),
    path('order/', order_show.order_show, name='order_show'),

]
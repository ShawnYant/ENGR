from django.urls import path
from Cart.views import cart_add,cart_detail,cart_remove

app_name = 'cart'

urlpatterns = [
    path('', cart_detail.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove.cart_remove, name='cart_remove'),
]

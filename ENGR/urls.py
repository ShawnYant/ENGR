"""ENGR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import Customer.views.Index
import Customer.views.Aftlogin
import Customer.views.Dologin
import Customer.views.Contact
import Customer.views.About
# from Store import views
from . import settings
from django.conf.urls.static import static
# from Cart import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Customer.views.Index.Index,name='index'),
    path('contact/', Customer.views.Contact.Contact,name='contact'),
    path('about/', Customer.views.About.About,name='about'),
    path('Customer/', include('Customer.urls') ),
    # path('dologin/', Customer.views.Dologin.dologin,name='Customer_dologin'),
    path('cart/', include('Cart.urls', namespace='cart')),
    path('orders/', include('Order.urls', namespace='orders')),
    path('payment/', include('Payment.urls', namespace='payment')),
    # path('cart/', views.cart_detail, name='cart_detail'),
    path('store/', include('Store.urls', namespace='store')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
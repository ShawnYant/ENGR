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
from Customer import views
# from Store import views
from django.conf import settings
from django.conf.urls.static import static
# from Cart import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('#', views.aftlogin,name='aftlogin'),
    path('Customer/', include('Customer.urls') ),
    path('dologin',views.dologin,name='Customer_dologin'),
    path('cart/', include('Cart.urls', namespace='cart')),
    # path('cart/', views.cart_detail, name='cart_detail'),
    path('', include('Store.urls', namespace='Store')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
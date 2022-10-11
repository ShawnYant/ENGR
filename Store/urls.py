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
from django.urls import path
from Store.views import restaurant_list
from Store.views import product_detail
from Store.views import product_list
from Store.views import search
app_name = 'store'
urlpatterns = [
    path('', restaurant_list.restaurant_list, name='restaurant_list'),
    path('<slug:category_slug>/', product_list.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail.product_detail,
         name='product_detail'),
    path('search',search.Search, name='store_dosearch'),
]
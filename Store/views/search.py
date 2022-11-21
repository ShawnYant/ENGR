from errno import errorcode
from multiprocessing import context
import traceback
from Store.models.Category import Category
from Store.models.Product import Product
from Store.models.Restaurant import Restaurant
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from Store.views import restaurant_list
from Customer.cuss import Cuss



def Search(request):

    try:
        name = request.POST['search']
        print(name)
        Q_Product = Product.objects.filter(slug__icontains=name)
        print(Q_Product)
        Q_Restaurant = Restaurant.objects.filter(slug__icontains=name)
        print(Q_Restaurant)
              
        return render(request, 'templates/web/Store/result.html',
                                {'resultP':Q_Product,
                                'resultR':Q_Restaurant,
                                'cus': Cuss.cuss_id})
    except:
        messages.error(request,'food does not exist!')
        traceback.print_exc()
        return render(request, 'templates/web/re-log/index.html', {'cus': Cuss.cuss_id} )

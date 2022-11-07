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

        # r= Q_Product and Q_Restaurant
              
        return render(request, 'templates/web/Store/result.html',
                                {'resultP':Q_Product,
                                'resultR':Q_Restaurant,
                                'cus': Cuss.cuss_id})

            # if name in Q_Restaurant:
            #     # context = {'result': Q_Restaurant}
            #     return render(request, 'templates/web/re-log/result.html',{'result':Q_Restaurant,
            #         'name': name,
            #         'categories': name.slug})
            # if name in Q_Catagory:
            #     # conext = {'result': Q_Catagory}
            #     return render(request, 'templates/web/re-log/result.html',{"result":Q_Catagory,
            #         'name': name,
            #         'categories': name.name})
            # if name in Q_Product:
            #     # context = {'result': Q_Product}
            #     return render(request, 'templates/web/re-log/result.html',{"result":Q_Product,
            #         'name': name,
            #         'restaurants': name.restaurant})
            # 
        print("it is here")

        
    except:
        messages.error(request,'food does not exist!')
        traceback.print_exc()
        return redirect(reverse('index'))

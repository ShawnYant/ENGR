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



def Search(request):

    try:
        name = request.POST['search']
        print(name)
        # _vals = {'name':name}
        # Q(slug__contains=name)
        # Q_Catagory = Category.objects.filter(slug__icontains=name)
        # print(Q_Catagory)
        Q_Product = Product.objects.filter(slug__icontains=name)
        print(Q_Product)
        Q_Restaurant = Restaurant.objects.filter(slug__icontains=name)
        print(Q_Restaurant)
        for r in Q_Restaurant or Q_Product:
            print(r)
            print(r.name)
            # print(r.category)
            print(r.get_absolute_url)
            
        # Q_Catagory = Category.objects.filter(name__contains=name)
        # Q_Product = Product.objects.filter(name__contains=name)
        # Q_Restaurant = Restaurant.objects.filter(name__contains=name)
        
        # categories = Category.objects.all()
        # restaurants = Restaurant.objects.all()
        for r in  Q_Product or Q_Restaurant:
            return render(request, 'templates/web/Store/result.html',
                                {'result':r})

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

        return errorcode
    except:
        messages.error(request,'food does not exist!')
        traceback.print_exc()
        return redirect(reverse('index'))

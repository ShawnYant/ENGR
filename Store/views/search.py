from errno import errorcode
import traceback
from Store.models.Category import Category
from Store.models.Product import Product
from Store.models.Restaurant import Restaurant
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.db.models import Q

def Search(request):

    try:
        name = request.POST['search']
        print(name)
        # _vals = {'name':name}
        # Q(slug__contains=name)
        Q_Catagory = Category.objects.filter(slug__icontains=name)
        print(Q_Catagory)
        Q_Product = Product.objects.filter(slug__icontains=name)
        print(Q_Product)
        Q_Restaurant = Restaurant.objects.filter(slug__icontains=name)
        print(Q_Restaurant)
        # Q_Catagory = Category.objects.filter(name__contains=name)
        # Q_Product = Product.objects.filter(name__contains=name)
        # Q_Restaurant = Restaurant.objects.filter(name__contains=name)

        for name in Q_Catagory or Q_Product or Q_Restaurant:
            if name in Q_Restaurant:
                return render(request, 'templates/web/re-log/resultRest.html')
            elif name in Q_Catagory:
                return render(request, 'templates/web/re-log/resultCata.html')
            elif name in Q_Product:
                return render(request, 'templates/web/re-log/resultFood.html')

            print("it is here")

        return errorcode
    except:
        traceback.print_exc()
        return redirect(reverse('index'))

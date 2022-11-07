from distutils.log import error
from re import L
from tkinter import END
from django.shortcuts import get_object_or_404, render
from Store.models.Category import Category
from Store.models.Product import Product
from Store.models.Restaurant import Restaurant
import MySQLdb
from Customer.cuss import Cuss


def List_all(request):
    list = Restaurant.objects.all()
   
    print(list)
    
    return render(request, 
                    'templates\web\Store\product\listall.html',
                   {'result':list,
                    'cus':Cuss.cuss_id})
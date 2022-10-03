from ast import Pass
from select import select
from sqlite3 import Cursor, connect
from django.shortcuts import redirect,render
from django.urls import reverse
from Customer.models.customer import Customer
from Customer.cuss import Cuss
from django.contrib import messages
import mysql.connector


def do_login(request):
    ''' perform the login operation'''
    # try:
    # db=mysql.connector.connect(host= "localhost", user="root", password="123qwe", database="ENGR",port="3306")
    # cursor = db.cursor()
    # query = ("SELECT customer From ENGR")
    user = Customer.objects.get(username=request.POST['username'])
    pa = request.POST['pass']
    # condition = cursor.fetchall(query)
    # for user in condition:
    if pa == user.password:
            Cuss.cuss_id = user.username
            print('login successfully')
            request.session['cuss'] = user.toDict()
            messages.error(request,'login is success!')
            return redirect(reverse('aft_login'))
    else:
            messages.error(request,'Wrong password!')
            return redirect(reverse('Customer_login'))
    # else:
    #     messages.error(request,'Wrong !')
    #     return redirect(reverse('Customer_login'))
    #     # except:
    #     #     return redirect(request,'Customer_login')

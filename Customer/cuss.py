from decimal import Decimal
from django.conf import settings
from pymysql import NULL
from Customer.models import customer
from datetime import datetime
# from unicodedata import name
# from django.shortcuts import redirect, render
from django.http import HttpResponse 
# from django.shortcuts import render
# from django.urls import reverse
# from shop.models import Product
class Cuss(object):
    cuss_id = NULL
    def __init__(self, request):
        """
        Initialize the cuss.
        """
        self.session = request.session
        cuss = self.session.get(settings.CUSS_SESSION_ID)
        if not cuss:
            # save an empty cuss in the session
            cuss = self.session[settings.CUSS_SESSION_ID] = {}
        self.cuss = cuss

    def add(self, nickname, email, address, phoneNo, birthdate):
        """
        Add a product to the cuss or update its information.
        """
        cuss_id = str(customer.userid)
        if cuss_id not in self.cuss:
            print('user does not exist')
            # self.cuss[cuss_id] = {'quantity': 0,
            #                          'price': str(product.price)}
        # else:
        #     self.cuss[cuss_id]['nickname'] = request.POST.get('username')
        # else:
        #     self.cuss[cuss_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    # def remove(self, product):
    #     """
    #     Remove a product from the cuss.
    #     """
    #     product_id = str(product.id)
    #     if product_id in self.cuss:
    #         del self.cuss[product_id]
    #         self.save()

    # def __iter__(self):
    #     """
    #     Iterate over the items in the cuss and get the products
    #     from the database.
    #     """
    #     Customer_id = self.cuss.keys()
    #     # get the product objects and add them to the cuss
    #     Customers = Customer.objects.filter(id__in=customer.userid)
    #     cuss = self.cuss.copy()
    #     for product in products:
    #         cuss[str(product.id)]['product'] = product
    #     for item in cuss.values():
    #         item['price'] = Decimal(item['price'])
    #         item['total_price'] = item['price'] * item['quantity']
    #         yield item

    # def __len__(self):
    #     """
    #     Count all items in the cuss.
    #     """
    #     return sum(item['quantity'] for item in self.cuss.values())

    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * item['quantity'] for item in self.cuss.values())


    def clear(self):
        # remove cuss from session
        del self.session[settings.cuss_SESSION_ID]
        self.save()


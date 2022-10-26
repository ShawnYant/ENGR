from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render
from Customer.cuss import Cuss
from Customer.models.customer import Customer

def Listinfo(request):
    uname=Cuss.cuss_id
    customer=Customer.objects.filter(username=uname)
    return render(request,"templates/web/re-log/info.html",
                    {'cus':uname,'user':customer})
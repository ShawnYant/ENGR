from unicodedata import name
from django.shortcuts import render
from Customer.cuss import Cuss
from Customer.models.customer import Customer

def Listinfo(request):
    uname = Cuss.cuss_id
    c = Customer.objects.filter(username=uname).values
    print(uname)
    print(c)
    return render(request,"templates/web/re-log/info.html",
                    {'cus':uname,'user':c})
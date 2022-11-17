from django.shortcuts import render
from Customer.cuss import Cuss
from Customer.models.customer import Customer

def Listinfo(request):
    uname = Cuss.cuss_id
    result = Customer.objects.get(username=uname)
    
    print(uname)
    print(result.username)
    return render(request,"templates/web/re-log/info.html",
                    {'cus':uname,'user':result})
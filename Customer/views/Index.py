from django.shortcuts import render
from Customer.cuss import Cuss
from Store.models.Restaurant import Restaurant

def Index(request):
    a=Cuss.cuss_id
    res=Restaurant.objects.all()

    return render(request,"templates/web/re-log/index.html",{'res':res,'cus':a})
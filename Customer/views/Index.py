from django.shortcuts import render
from django.shortcuts import render
from Customer.cuss import Cuss

def Index(request):
    a=Cuss.cuss_id
    return render(request,"templates/web/re-log/index.html",{'cus':a})
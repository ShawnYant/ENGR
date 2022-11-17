from django.shortcuts import render
from Customer.cuss import Cuss

def About(request):
    a=Cuss.cuss_id
    return render(request,"templates/web/about.html",{'cus':a})
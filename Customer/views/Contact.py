from django.shortcuts import render
from Customer.cuss import Cuss

def Contact(request):
    a=Cuss.cuss_id
    return render(request,"templates/web/contact.html",{'cus':a})
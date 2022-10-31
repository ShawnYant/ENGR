from django.shortcuts import render
from django.shortcuts import render
from Customer.cuss import Cuss

def Login(request):
    '''load the login form'''
    a=Cuss.cuss_id
    return render(request,"templates/web/re-log/login.html",{'cus':a})
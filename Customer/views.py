from ctypes import GetLastError
from datetime import datetime
from re import A
from unicodedata import name
from webbrowser import get
from django.shortcuts import redirect, render

from django.http import HttpResponse 
from django.shortcuts import render
from django.urls import reverse
from mysqlx import Session
from Customer import cuss

from Customer.models import customer,payment
from Customer.cuss import Cuss
from django.contrib import messages
# Create your views here.



def regist(request):
    '''load the regit form'''
    # return render(request,'web/ re-log/ register.html')
    return render(request,'templates/web/re-log/register.html')

   

def doregist(request):
    ''' Execute order adding '''
    try:
        ob=customer()
        ob.username = request.POST.get('username')
        ob.password = request.POST.get('password')
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        messages.error(request,'Registration is success!')
        context = {'info':"Successfully Add!!"}
        return redirect(reverse('index'))

    except Exception as err:
        print(err)
        context = {'info':"Add Failed!!"}   
        return render(request,'templates/web/re-log/register.html',) 


def Update(request):
    #render the update page
    return render(request,'templates/web/re-log/update.html',) 


def DoUpdate(request):
        try:
            print("username")
            print(Cuss.cuss_id)
            ob=customer.objects.get(username=Cuss.cuss_id)
            ob.nickname = request.POST.get('nickname')
            ob.email = request.POST.get('email')
            ob.phoneNo = request.POST.get('phoneNo')
        # ob.birthdate = request.POST.get('birthdate')
            ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()
            print('123 123')
            context = {'info':"Successfully Add!!"}
            return redirect(reverse('aftlogin'))
    
        except Exception as err:
            err.with_traceback()
            print(err.__traceback__)
            context = {'info':"Add Failed!!"}   
            return render(request,'templates/web/re-log/update.html',) 



def Payment(request):
    try:
        ob=payment()
        ob.cardnumber = request.POST.get('username')
        ob.secureNo = request.POST.get('password')
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()

        context = {'info':"Successfully Add!!"}
        return render(request,'web\ re-log\ register.html',)

    except Exception as err:
        print(err)
        context = {'info':"Add Failed!!"}   
        return render(request,'web\ re-log\ register.html',) 


def login(request):
    '''load the login form'''
    return render(request,"templates/web/re-log/login.html")

def dologin(request):
    ''' perform the login operation'''
    user = customer.objects.get(username=request.POST['username'])
    pa = request.POST['pass']
    if pa == user.password:
        Cuss.cuss_id = user.username
        print('login successfully')
        request.session['cuss'] = user.toDict()
        messages.error(request,'login is success!')
        return redirect(reverse('aftlogin'))
    else:
        return redirect(request,'Customer_login'+"login fail")

    # try:
    #     if request.POST['code'] != request.session['verifycode']:
    #         return redirect(reverse('web_login')+"?errinfo=2")

    #     #Obtain user information based on login account
    #     user = customer.objects.get(username=request.POST['username'])
    #     Word = request.POST['pass']
    #         #Check whether the current user is valid or an administrator
    #     if  user.status == 1 or user.status == 6:
    #         #identify whether the password is valid
    #         # import hashlib
    #         # md5 = hashlib.md5()
    #         # s = request.POST['pass']+user.password_salt #Get the password from the form and add an interference value
    #         # md5.update(s.encode('utf-8')) 
            
    #         if Word == user.password  :
    #             print('login successfully!')
    #             request.session['webuser'] = user.toDict()
    #             return redirect(reverse('web_index'))
    #         else:
    #            return redirect(reverse('web_login')+"?errinfo=5")

    #     else :
    #         return redirect(reverse('web_login')+"?errinfo=4")
    # except Exception as err:
    #     print(err)
    #     return redirect(reverse('web_login')+"?errinfo=3")
  
def index(request):

    return render(request,"templates/web/re-log/index.html")

def aftlogin(request):

    return render(request,"templates/web/re-log/aftlogin.html")


def logout(request):
    ''' perform the logout operation'''
    del request.session['customer']
    return redirect(reverse('Customer_login'))
from django.shortcuts import redirect
from django.urls import reverse
from Customer.models.customer import customer
from Customer.cuss import Cuss
from django.contrib import messages

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
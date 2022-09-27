from django.shortcuts import redirect,render
from django.urls import reverse
from Customer.models.customer import Customer
from Customer.cuss import Cuss
from django.contrib import messages


def do_login(request):
    ''' perform the login operation'''
    # try:
    user = Customer.objects.get(username=request.POST['username'])
    pa = request.POST['pass']
    if pa == user.password:
        Cuss.cuss_id = user.username
        print('login successfully')
        request.session['cuss'] = user.toDict()
        messages.error(request,'login is success!')
    return redirect(reverse('aft_login'))
        # else:
        #         return redirect(request,'Customer_login')
    # except:
    #     return redirect(request,'Customer_login')

from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import auth

from Customer.cuss import Cuss
from Customer.models.customer import Customer
from ENGR import settings

def Logout(request):
    ''' perform the logout operation'''
    # try:
    # a=request.session['cuss']
    # if Cuss.cuss_id:
    # # for Cuss.cuss_id in request.session.keys():
    #     Cuss.clear
    # elif a:
    del request.session['cuss']
            # request.session.delete()
    # print(request.session['cuss'])
    Cuss.cuss_id = None
    print(Cuss.cuss_id)
    return render ( request,'templates/web/re-log/login.html', { 'cus' : Cuss.cuss_id})
        # user = getattr(request, 'user', None)
    # if hasattr(user, 'is_authenticated') and not user.is_authenticated():
    #     user = None
    # Customer.send(sender=user.__class__, request=request, user=user)

    # request.session.flush()
    # if hasattr(request, 'user'):
    #     from django.contrib.auth.models import AnonymousUser
    #     request.user = AnonymousUser()
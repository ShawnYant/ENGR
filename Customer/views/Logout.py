from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import auth

from Customer.cuss import Cuss
from Customer.models.customer import Customer
from ENGR import settings

def Logout(request):
    ''' perform the logout operation'''
    
    # for sesskey in request.session.keys():
    del request.session['cuss']
    auth.logout(request)
    return redirect(reverse('index'))
    # user = getattr(request, 'user', None)
    # if hasattr(user, 'is_authenticated') and not user.is_authenticated():
    #     user = None
    # Customer.send(sender=user.__class__, request=request, user=user)

    # request.session.flush()
    # if hasattr(request, 'user'):
    #     from django.contrib.auth.models import AnonymousUser
    #     request.user = AnonymousUser()
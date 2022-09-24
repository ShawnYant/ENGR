from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import auth

from Customer.cuss import Cuss


def Logout(request):
    ''' perform the logout operation'''
    auth.logout(request)
    request.session.flush()
    return redirect(reverse('index'))
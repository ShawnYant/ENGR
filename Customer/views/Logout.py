from django.shortcuts import redirect
from django.urls import reverse


def logout(request):
    ''' perform the logout operation'''
    del request.session['customer']
    return redirect(reverse('Customer_login'))
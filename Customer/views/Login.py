from django.shortcuts import render
from django.shortcuts import render


def login(request):
    '''load the login form'''
    return render(request,"templates/web/re-log/login.html")
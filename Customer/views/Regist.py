from django.shortcuts import render
from django.shortcuts import render


def regist(request):
    '''load the regit form'''
    # return render(request,'web/ re-log/ register.html')
    return render(request,'templates/web/re-log/register.html')

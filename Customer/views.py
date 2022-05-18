from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse 
from django.shortcuts import render

from Customer.models import customer 


# Create your views here.



def regist(request):
    '''load the regit form'''
    return render(request,"web\ re-log\ register.html")


    

def doregist(request):
    ''' Execute order adding '''
    try:
        ob=customer()
        ob.username = request.POST.get('username')
        ob.password = request.POST.get('password')
        ob.email = request.POST.get('email')
        ob.phoneNo = request.POST.get('phoneNo')
        ob.address = ""
        ob.nickname = ""
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()

        context = {'info':"Successfully Add!!"}
        return render(request,'web\index.html',)

    except Exception as err:
        print(err)
        context = {'info':"Addition Failed!!"}   
        return render(request,'web\Regist.html',) 

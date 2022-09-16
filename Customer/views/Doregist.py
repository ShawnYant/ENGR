from datetime import datetime
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.urls import reverse
from Customer.models.customer import customer
from django.contrib import messages

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

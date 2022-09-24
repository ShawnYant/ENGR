from datetime import datetime
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.urls import reverse
from Customer.models.customer import Customer
from django.contrib import messages

def do_regist(request):
    ''' Execute order adding '''
    try:
        ob=Customer()
        ob.username = request.POST.get('username')
        ob.password = request.POST.get('password')
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        messages.error(request,'Registration is success!')
        # context = {'info':"Successfully Add!!"}
        return redirect(reverse('index'))

    except Exception as err:
        print(err)
        messages.error(request,'Registration is fail!')
        # context = {'info':"Add Failed!!"}   
        return render(request,'templates/web/re-log/register.html',) 

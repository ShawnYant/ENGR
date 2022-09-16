from datetime import datetime
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.urls import reverse
from Customer.models.customer import customer
from Customer.cuss import Cuss
from django.contrib import messages

def DoUpdate(request):
        try:
            print("username")
            print(Cuss.cuss_id)
            ob=customer.objects.get(username=Cuss.cuss_id)
            ob.nickname = request.POST.get('nickname')
            ob.email = request.POST.get('email')
            ob.address = request.POST.get('address')
            ob.phoneNo = request.POST.get('phoneNo')
            ob.birthdate = request.POST.get('birthdate')
            ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            messages.error(request,'update is success!')
            ob.save()
            print('123 123')
            context = {'info':"Successfully Add!!"}
            return redirect(reverse('aftlogin'))

        except Exception as err:
            err.with_traceback()
            # print(customer.unique_error_message)
            print(err.__traceback__)
            context = {'info':"Add Failed!!"}   
            return render(request,'templates/web/re-log/update.html',) 

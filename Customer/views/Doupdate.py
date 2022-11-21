from datetime import datetime
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.urls import reverse
from Customer.models.customer import Customer
from Customer.cuss import Cuss
from django.contrib import messages

def do_Update(request):
        try:
            b=Cuss.cuss_id
            print('username')
            print(b)
            ob=Customer.objects.get(username=request.session.get('cuss'))
            ob.nickname = request.POST.get('nickname')
            ob.email = request.POST.get('email')
            ob.address = request.POST.get('address')
            ob.phoneNo = request.POST.get('phoneNo')
            ob.birthdate = request.POST.get('birthdate')
            ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            messages.error(request,'update is success!')
            ob.save()
         
            context = {'info':"Successfully Add!!"}
            return render(request,'templates/web/re-log/index.html',{'cus':b})

        except Exception as err:
            # err.with_traceback()
            # # print(customer.unique_error_message)
            # print(err.__traceback__)
            context = {'info':"Add Failed!!"}   
            return render(request,'templates/web/re-log/update.html',) 

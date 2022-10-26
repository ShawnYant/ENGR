from django.shortcuts import redirect,render
from django.urls import reverse
from Customer.models.customer import Customer
from Customer.cuss import Cuss
from django.contrib import messages
import traceback



def do_login(request):
    ''' perform the login operation'''
    try:
       
        user = Customer.objects.get(username=request.POST['username'])
        pa = request.POST['pass']
        if pa == user.password:
                Cuss.cuss_id = user.username
                print('login successfully')
                request.session['cuss'] = user.username
                a=request.session['cuss']
                print(a)
                messages.error(request,'login is success!')
                return render(request,'templates/web/re-log/aft_login.html',{'cus':Cuss.cuss_id})
                
        else:
                messages.error(request,'Wrong password!')
                return redirect(reverse('Customer_login'))
        # else:
        #     messages.error(request,'Wrong !')
        #     return redirect(reverse('Customer_login'))
        
    except:
        traceback.print_exc()
        messages.error(request,'User does not exist!')
        return redirect(reverse('Customer_login'))

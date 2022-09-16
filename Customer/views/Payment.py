from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render
from Customer.models.payment import payment

def Payment(request):
    try:
        ob=payment()
        ob.cardnumber = request.POST.get('username')
        ob.secureNo = request.POST.get('password')
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()

        context = {'info':"Successfully Add!!"}
        return render(request,'web\ re-log\ register.html',)

    except Exception as err:
        print(err)
        context = {'info':"Add Failed!!"}   
        return render(request,'web\ re-log\ register.html',) 
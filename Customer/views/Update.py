from django.shortcuts import render
from django.shortcuts import render
from Customer.cuss import Cuss


def Update(request):
    #render the update page
    a=Cuss.cuss_id
    return render(request,'templates/web/re-log/update.html',{'cus':a}) 
from django.shortcuts import render

# Create your views here.
def index(request):
    ''' Ordering System Homepage'''
    return render(request,"templates/web/re-log/index.html")
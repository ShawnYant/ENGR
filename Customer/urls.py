"""ENGR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Customer.views import Dologin,Doregist,Doupdate,Login,Update



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', Doregist.doregist, name='Customer_doregister'),
    path('update',Update.Update, name='Customer_update'),
    path('DoUpdate', Doupdate.DoUpdate, name='Customer_DoUpdate'),
    path('login', Login.login, name='Customer_login'),
    path('dologin', Dologin.dologin, name='Customer_dologin'),
    

]

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
from Customer.views import Aftlogin,Dologin,Doregist,Doupdate,Login,Update,Logout,Regist,Listinfo
from Store.views import search
# from Customer.views.Doregist import do_regist
# from Customer.views.Regist import Regist



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Regist.Regist,name='Customer_register'),
    path('regist',Doregist.do_regist,name='Customer_doregister'),
    path('update',Update.Update, name='Customer_update'),
    path('DoUpdate', Doupdate.do_Update, name='Customer_DoUpdate'),
    path('login', Login.Login, name='Customer_login'),
    path('dologin', Dologin.do_login, name='Customer_dologin'),
    path('logout', Logout.Logout, name='Customer_logout'),
    path('#',Aftlogin.aft_login,name='aft_login'),
    path('search',search.Search, name='Store_dosearch'),
    path('listinfo',Listinfo.Listinfo, name='Customer_listinfo'),
    ]

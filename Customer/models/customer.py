from django.db import models
from datetime import datetime


class Customer(models.Model):
    userid = models.IntegerField(default=1)                       #ID
    username = models.CharField(max_length=50)                 #Account
    password = models.CharField(max_length=100, default='123') #password
    create_at = models.DateTimeField(default=datetime.now)    #creat time
    nickname = models.CharField(max_length=50)    #nickname
    email = models.EmailField(unique=False,default='null') # EMAIL
    address = models.CharField(max_length=1000,default='')   #customer address
    phoneNo = models.CharField(max_length=1000,default='')  #customer phone number
    birthdate = models.DateField(null=True)
    # birthdate = models.DateTimeField(max_length=10,default= datetime.now)  #customer date of birth
    status = models.IntegerField(default=1)    #Status:pending for next sprint
    update_at = models.DateTimeField(null=True)    #update time

    
    def toDict(self):
        return {'userid':self.userid,'username':self.username,'password':self.password,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'nickname':self.nickname,'email':self.email,'address':self.address,'phoneNo':self.phoneNo,'birthdate':self.birthdate.strftime('%Y-%m-%d %H:%M:%S'),'status':self.status,'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S'),} 
    class Meta:
        db_table = "customer"  # change the name of the table
from django.db import models
from datetime import datetime



class customer(models.Model):
    username = models.CharField(max_length=50)    #Account
    password = models.CharField(max_length=100, default='123') #password
    create_at = models.DateTimeField(default=datetime.now)    #creat time
    update_at = models.DateTimeField(default=datetime.now)    #update time

    
    def toDict(self):
        return {'id':self.id,'username':self.username,'password':self.password,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),} 
    class Meta:
        db_table = "customer"  # change the name of the table



class update(models.Model):
    nickname = models.CharField(max_length=50)    #nickname
    email = models.EmailField(unique= True,default='123@123.com') # EMAIL
    address = models.CharField(max_length=100,default='123')   #customer address
    phoneNo = models.CharField(max_length=10,default='123')  #customer phone number
    birthdate = models.DateTimeField(max_length=10,default=datetime.now)  #customer date of birth
    status = models.IntegerField(default=1)    #Status:pending for next sprint

    def toDict(self):
        return {'nickname':self.nickname,'email':self.email,'address':self.address,'phoneNo':self.phoneNo,'status':self.status,'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S'),} 
    class Meta:
        db_table = "customer_up"  # change the name of the table


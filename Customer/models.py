from django.db import models
from datetime import date, datetime
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession


# class CustomSession(AbstractBaseSession):
#     account_id = models.IntegerField(null=True, db_index=True)

#     @classmethod
#     def get_session_store_class(cls):
#         return SessionStore

# class SessionStore(DBStore):
#     @classmethod
#     def get_model_class(cls):
#         return CustomSession

#     def create_model_instance(self, data):
#         obj = super().create_model_instance(data)
#         try:
#             account_id = int(data.get('_auth_user_id'))
#         except (ValueError, TypeError):
#             account_id = None
#         obj.account_id = account_id
#         return obj

class customer(models.Model):
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
        return {'userid':self.userid,'username':self.username,'password':self.password,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'nickname':self.nickname,'email':self.email,'address':self.address,'phoneNo':self.phoneNo,'birthdate':self.birthdate,'status':self.status,'update_at':self.update_at,} 
    class Meta:
        db_table = "customer"  # change the name of the table



# class update(models.Model):
#     updateid = models.IntegerField(default=1)
#     nickname = models.CharField(max_length=50)    #nickname
#     email = models.EmailField(unique= True,default='123@123.com') # EMAIL
#     address = models.CharField(max_length=100,default='123')   #customer address
#     phoneNo = models.CharField(max_length=10,default='123')  #customer phone number
#     birthdate = models.DateTimeField(max_length=10,default=datetime.now)  #customer date of birth
#     status = models.IntegerField(default=1)    #Status:pending for next sprint
#     update_at = models.DateTimeField(default=datetime.now)    #update time

#     def toDict(self):
#         return {'updateid':self.updateid,'nickname':self.nickname,'email':self.email,'address':self.address,'phoneNo':self.phoneNo,'status':self.status,'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S'),} 
#     class Meta:
#         db_table = "customer_up"  # change the name of the table


class payment(models.Model):
    cardnumber = models.CharField(max_length=100)    #cardnumber
    secureNo = models.CharField(max_length= 5)       #security number
    # customerID = models.IntegerField()                 #to pare with the id in class customer
    create_at = models.DateTimeField(default=datetime.now)    #creat time
    update_at = models.DateTimeField(default=datetime.now)    #update time


    def toDict(self):
        return {'cardnumber':self.cardnumber,'secureNo':self.secureNo,'customerID':self.customerID,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S'),} 
    class Meta:
        db_table = "payment"  # change the name of the table

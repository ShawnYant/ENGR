from django.db import models
from datetime import datetime

class Payment(models.Model):
    cardnumber = models.CharField(max_length=100)    #cardnumber
    secureNo = models.CharField(max_length= 5)       #security number
    # customerID = models.IntegerField()                 #to pare with the id in class customer
    create_at = models.DateTimeField(default=datetime.now)    #creat time
    update_at = models.DateTimeField(default=datetime.now)    #update time


    def toDict(self):
        return {'cardnumber':self.cardnumber,'secureNo':self.secureNo,'customerID':self.customerID,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S'),} 
    class Meta:

        db_table = "payment"  # change the name of the table

from django.db import models

# Create your models here.
from django.db import models
from Customer.cuss import Cuss

from Customer.models.customer import Customer


class Order(models.Model):
    if Cuss.cuss_id == None:
        username = models.CharField(max_length=50) 
        nickname = models.CharField(max_length=50)
        email = models.EmailField()
        address = models.CharField(max_length=250)
        postal_code = models.CharField(max_length=20)
        city = models.CharField(max_length=100)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        paid = models.BooleanField(default=False)
        braintree_id = models.CharField(max_length=150, blank=True)
        class Meta:
            ordering = ('-created',)
    if Cuss.cuss_id:
        ping = Customer.objects.get(username=Cuss.cuss_id)
        print(ping)    
        username = ping.username 
        nickname = ping.nickname
        email = ping.email
        address = ping.address
        postal_code = models.CharField(max_length=20)
        city = models.CharField(max_length=100)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        paid = models.BooleanField(default=False)
        braintree_id = models.CharField(max_length=150, blank=True)
        class Meta:
            ordering = ('-created',)


 

    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
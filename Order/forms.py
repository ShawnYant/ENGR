from django import forms
from Customer.cuss import Cuss
from Customer.models.customer import Customer
from .models.Order import Order

class OrderCreateForm(forms.ModelForm):
 
    class Meta:
        model = Order
        fields = ['username', 'nickname', 'email', 'address',
                'postal_code', 'city']




            



                         
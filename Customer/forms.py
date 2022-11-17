from django import forms

from .models.customer import Customer

class CustomerinfoForm(forms.ModelForm):
 
    class Meta:
        model = Customer
        fields = ['nickname', 'email', 'address',

         ]




            



                         
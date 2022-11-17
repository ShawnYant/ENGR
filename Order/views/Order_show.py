from django.shortcuts import get_object_or_404, render
from Store.models.Product import Product
from Order.models.Order import Order
from Order.models.OrderItem import OrderItem
from Customer.models.customer import Customer
from Customer.cuss import Cuss
import pickle


def order_show(request):

    if Cuss.cuss_id:
        # query = pickle.loads()
        # cus=Customer.objects.get(username=Cuss.cuss_id)
        # orderinfo=Order.objects.filter(username=Cuss.cuss_id)
        # orderid=Order.objects.filter(username=Cuss.cuss_id).values('id')
        # order=OrderItem.objects.filter(order_id=orderid)
        # orderid2=OrderItem.objects.filter(order_id=orderid).values('product_id')
        # item=Product.objects.filter(id=orderid2)

        cus=Customer.objects.get(username=Cuss.cuss_id)
        order=Order.objects.filter(username=Cuss.cuss_id)
        item=OrderItem.objects.filter(order_id=order)
        product=Product.objects.filter(id=item)

        context={'user':cus,
                 'order':order,
                 'item':item,
                 'product':product,
                 'cus':Cuss.cuss_id}


        return render(request,'templates/web/Order/showorder.html',context)

    else:

        pass

        # return render(request,''), make a redirct page with username enter, 
        # then redirect to the showorder page by using the entered name, also as those two
        # variables above.
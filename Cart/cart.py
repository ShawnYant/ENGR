from decimal import Decimal
import json
from xml.etree.ElementTree import tostring
from django.conf import settings
# from ENGR.settings import DecimalEncoder
from Store.models.Product import Product
from django.shortcuts import get_object_or_404


class Cart(object):


    # class DecimalEncoder(json.JSONEncoder):
    #     def default(self, obj):
    #     #if passed in object is instance of Decimal
    #     # convert it to a string
    #         if isinstance(obj, Decimal):
    #             return str(obj)
    #     # otherwise use the default behavior
    #         return json.JSONEncoder.default(self, obj)
        

    def __init__(self, request):
        """
        Initialize the cart.
        """
        print("init")
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart



    def __iter__(self):
        """

        Iterate over the items in the cart and get the products
        from the database.
        """
        print("iter")
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        # products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        print("iter-2")
        for id in product_ids:
            product = get_object_or_404(Product,
                                id=id,                               
                                available=True)
            print(str(product.id))
            #cart[str(product.id)]['product'] = product
            cart[str(product.id)]['id'] = product.id
            cart[str(product.id)]['image_url'] = product.image.url
            print(product.image.url)
            cart[str(product.id)]['get_absolute_url'] = product.get_absolute_url()
            cart[str(product.id)]['price'] = str(product.price)
            cart[str(product.id)]['name'] = product.name
            print("iter_3")
        # for item in cart.values():
            print(str(product.price))
            print(str(cart[str(product.id)]['quantity']))
            cart[str(product.id)]['total_price'] = str(product.price * cart[str(product.id)]['quantity'])

            print(cart[str(product.id)]['total_price'])
            print(product.toDict())
            
            yield  cart[str(product.id)]

    def __len__(self):
        """
        Count all items in the cart.
        """
        print("len")
        return sum(item['quantity'] for item in self.cart.values())


    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        print("add")
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

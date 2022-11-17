from django.db import models
from django.urls import reverse
from Store.models.Restaurant import Restaurant


class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def toDict(self):
        return {'restaurant':self.restaurant,'name':self.name, 'slug':self.slug, 'image':self.image, 'description':self.description,'price':str(self.price), 'available':self.available,'created':self.created.strftime('%Y-%m-%d %H:%M:%S'),'updated':self.updated.strftime('%Y-%m-%d %H:%M:%S')} 

    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug', 'id']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.name

    

    def get_absolute_url(self):
        return reverse('store:product_detail',
                       args=[self.id, self.slug])




from django.db import models
from django.urls import reverse
from Store.models.Category import Category

class Restaurant(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    # price = models.DecimalField(max_digits=10,
    #                             decimal_places=2)
    # # models.FloatField(max_length=200)
    # # models.Field(max_digits=10,decimal_places=1)
    # # models.CharField(max_length=200)
    # available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=200,default='null')

    def toDict(self):
        return {'category':self.category,'name':self.name, 'slug':self.slug, 'image':self.image, 'description':self.description,'created':self.created.strftime('%Y-%m-%d %H:%M:%S'),'updated':self.updated.strftime('%Y-%m-%d %H:%M:%S'),'address':self.address} 
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:restaurant_list',
                       args=[self.slug])

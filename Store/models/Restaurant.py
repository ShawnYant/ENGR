from django.db import models
from django.urls import reverse
from Store.models.Category import Category

class Restaurant(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='restaurants',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='restaurant/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=200,default='null')

    def toDict(self):
        return {'category':self.category,'name':self.name, 'slug':self.slug, 'image':self.image, 'description':self.description,'created':self.created.strftime('%Y-%m-%d %H:%M:%S'),'updated':self.updated.strftime('%Y-%m-%d %H:%M:%S'),'address':self.address} 
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:restaurant_detail',
                       args=[self.slug,self.id])

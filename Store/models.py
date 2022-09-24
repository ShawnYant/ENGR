from django.db import models
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_list_by_category',
                       args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    # models.FloatField(max_length=200)
    # models.Field(max_digits=10,decimal_places=1)
    # models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def toDict(self):
        return {'category':self.category,'name':self.name, 'slug':self.slug, 'image':self.image, 'description':self.description,'price':str(self.price), 'available':self.available,'created':self.created.strftime('%Y-%m-%d %H:%M:%S'),'updated':self.updated.strftime('%Y-%m-%d %H:%M:%S')} 
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail',
                       args=[self.id, self.slug])

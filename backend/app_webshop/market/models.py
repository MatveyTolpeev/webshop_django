from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Provider(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)

class Consumer(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    address = models.TextField()
    geo_location = models.CharField(max_length=250, default='')

class Category(models.Model):
    name = models.CharField(max_length=250, default='')

class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)

class Store(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):

    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order'),
    )

    consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=250, default='new', choices=STATUS)

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=0)



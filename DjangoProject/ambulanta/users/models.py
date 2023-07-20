from django.db import models

"""# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY= (
    ('Indoor', 'indoor'),
    ('out Door', 'out Door'),
    )
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True, blank=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    tags= models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('pading', 'pading'),
        ('Out for delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product= models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS)"""
    
class Register(models.Model):
    name=models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    password1=models.CharField(max_length=200, null=False)
    password2=models.CharField(max_length=200, null=False)
    
    

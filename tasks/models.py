from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

CATEGORY_PRODUCTS = (
    ('H','Herramientas'),
    ('S','Seguridad'),
    ('M','Materiales')
)



# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    detecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.title + '- by ' + self.user.username

<<<<<<< HEAD

=======
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_PRODUCTS, max_length=1)

    def __str__(self):
        return self.title

class OrderProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.title() 

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username()
>>>>>>> Jeneby

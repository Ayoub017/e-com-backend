from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import AbstractBaseUser



# Create your models here.


class Person(AbstractUser):
    # account = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    adress = models.TextField(null=False)
    phone_number = models.CharField(null=False,unique=True,max_length=20)
    lat_pos = models.FloatField(null=False,default=0)
    long_pos = models.FloatField(null=False,default=0)
    type = models.CharField(null=False,max_length=10,default='client')
    

    
    

class Product(models.Model):
    category = models.CharField(max_length=80)
    titre = models.TextField(max_length=60)
    price = models.FloatField(max_length=60,null=True)
    image = models.TextField(null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
   

    

class Commande(models.Model):
    client = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='client')
    cuisinier =  models.ForeignKey(Person, on_delete=models.CASCADE,related_name='cuisinier')
    date = models.TextField()
    product = models.ManyToManyField(Product)
    price_total = models.FloatField(max_length=90)
    status = models.CharField(max_length=80)


    
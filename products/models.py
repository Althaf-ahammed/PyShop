from django.db import models
from django.forms import FloatField

class Product(models.Model):
    name=models.CharField(max_length=225)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=150)
class Offers(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=150)
    discount=models.FloatField(default=0)
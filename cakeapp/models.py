from django.db import models

# Create your models here.
class Cake(models.Model):
    cake_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    flavour=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.FileField()

class User(models.Model):
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    photo=models.FileField()
    address=models.CharField(max_length=100)

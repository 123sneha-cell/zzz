from django.db import models

# Create your models here.
class Cake(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.is_valid = None

    cake_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    flavour=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    image=models.FileField()

class User(models.Model):
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

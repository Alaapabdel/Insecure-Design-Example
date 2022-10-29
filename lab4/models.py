from django.db import models

# Create your models here.
class User(models.Model):
    userID= models.IntegerField()
    name= models.CharField(max_length=100)
    cc= models.CharField(max_length=19)
    pin= models.IntegerField()

class Branch(models.Model):
    country= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    street= models.CharField(max_length=100)
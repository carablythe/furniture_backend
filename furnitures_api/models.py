from django.db import models

# Create your models here.
class Furniture(models.Model):
    name = models.CharField(max_length = 32)
    img = models.TextField()
    color = models.CharField(max_length = 20, default = 'white')
    category = models.CharField(max_length = 32)
    price = models.IntegerField()
    quantity = models.IntegerField(default = 1)
    availability = models.BooleanField()

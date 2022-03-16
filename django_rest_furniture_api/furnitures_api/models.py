from django.db import models

# Create your models here.
class Furniture(models.Model):
    name = models.CharField(max_length = 32)
    img = models.TextField()
    category = models.CharField(max_length = 32)
    price = models.IntegerField()
    availability = models.BooleanField()

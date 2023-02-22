from django.db import models
from django.contrib.auth.models  import User #this model is already existed, how we create the superuser
from django.core.validators import MaxValueValidator, MinValueValidator #this allows for a 5-star rating system in the Customer Review Section

class Furniture(models.Model):
    name = models.CharField(max_length = 32)
    img = models.ImageField(null = True, blank = True )
    imgURL = models.TextField (null = True, blank = True)
    color = models.CharField(max_length = 20)
    category = models.CharField(max_length = 32)
    price = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank = True)
    quantity = models.IntegerField(default = 1)
    availability = models.BooleanField()
    orderQuantity = models.IntegerField(default = 1)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    def __str__(self): #this will display the items in the database by the name instead of just the furniture 1, furniture 2, etc...
        return self.name

class Review (models.Model):
    product = models.ForeignKey(Furniture, on_delete = models.SET_NULL, null = True)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    rating = models.IntegerField(default = 0)
    validators=[MaxValueValidator(5), MinValueValidator(0)]
    comment = models.TextField(null = True, blank = True, max_length = 300)

    def __str__(self):
        return str(self.product)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    img = models.ImageField(null = True, blank = True )
    imgURL = models.CharField(max_length = 50, null = True, blank = True)
    price = models.IntegerField(default = 0)
    orderQuantity = models.IntegerField(default = 1)
    quantity = models.ForeignKey(Furniture, on_delete = models.SET_NULL, null = True)
    availability = models.BooleanField(default = True)
    color = models.CharField(max_length = 20, null = True, blank = True)
    category = models.CharField(max_length = 32, null = True, blank = True)
    name = models.CharField(max_length = 32, null = True, blank = True)



    def __str__(self):
        return str(self.user)

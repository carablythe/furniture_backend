from django.db import models
from django.contrib.auth.models  import User #this model is already existed, how we create the superuser

# Create your models here.
class Furniture(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    #the ForeignKey help to set one to many relationship, on_delete set to null to aviod the child elements getting delete if the parent element get deleted
    name = models.CharField(max_length = 32)
    img = models.ImageField(null = True, blank = True )
    imgURL = models.TextField (null = True, blank = True)
    color = models.CharField(max_length = 20, default = 'white')
    category = models.CharField(max_length = 32)
    price = models.IntegerField()
    quantity = models.IntegerField(default = 1)
    availability = models.BooleanField()


    def __str__(self): #this will display the items in the database by the name instead of just the furniture 1, furniture 2, etc...
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    paymentMethod = models.CharField(max_length = 200, null = True, blank = True)
    taxPrice = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank = True)
    shippingPrice = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank = True)
    totalPrice  = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank = True)
    isPaid = models.BooleanField(default = False)
    paidAt = models.DateTimeField (auto_now_add = False, null = True, blank = True)
    isDelivered = models.BooleanField(default = False)
    deliveredAt = models.DateTimeField (auto_now_add = False, null = True, blank = True)


    def __str__(self):
        return str(self.user)

class OrderItem (models.Model):
    product = models.ForeignKey(Furniture, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 200, null = True, blank = True)
    qty = models.IntegerField(null = True, blank = True, default = 0)
    price  = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank = True)
    img = models.TextField (null = True, blank = True)

    def __str__(self):
        return str(self.name)

class ShippingAddress (models.Model):
    order = models.OneToOneField(Order, on_delete = models.CASCADE, null = True, blank = True)
     #cascade means s.o deleted their order the shipping address will be gone with it
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 200, null = True, blank = True)
    postalCode = models.CharField(max_length = 5, null = True, blank = True)
    state = models.CharField(max_length = 2, null = True, blank = True)
    shippingPrice = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank = True)

    def __str__(self):
        return str(self.address)

class Review (models.Model):
    product = models.ForeignKey(Furniture, on_delete = models.SET_NULL, null = True)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    comment = models.TextField (null = True, blank = True)

    def __str__(self):
        return str(self.product)

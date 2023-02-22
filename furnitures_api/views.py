from django.shortcuts import render
from rest_framework import generics
from .serializers import FurnitureSerializer, CartSerializer, ReviewSerializer
from .models import Furniture, Cart, Review

class FurnitureList(generics.ListCreateAPIView):
    queryset = Furniture.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = FurnitureSerializer # tell django what serializer to use

class FurnitureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all().order_by('id')
    serializer_class = FurnitureSerializer

#######CartSerializer#######
class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = CartSerializer # tell django what serializer to use

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer

#####Review#####
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ReviewSerializer # tell django what serializer to use

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

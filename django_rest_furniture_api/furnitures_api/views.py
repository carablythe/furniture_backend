from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import FurnitureSerializer
from .models import Furniture

class FurnitureList(generics.ListCreateAPIView):
    queryset = Furniture.objects.all().order_by('id')
    serializer_class = FurnitureSerializer

class FurnitureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all().order_by('id')
    serializer_class = FurnitureSerializer

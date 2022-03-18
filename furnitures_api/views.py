from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import FurnitureSerializer, UserSerializer
from .models import Furniture

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
#serialize token, this is from simple jwt documentation

from rest_framework.decorators import api_view
from rest_framework.response import Response


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate (self, attrs): #we overide the validate method and serialize the user data, so that when we work with the frontend we dont have to decode the return json information, instead we have the username and email easy to reach
        data = super().validate(attrs)

        data['username'] = self.user.username
        data['email'] = self.user.email


        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer #the serializer class will actually return back the user data


class FurnitureList(generics.ListCreateAPIView):
    queryset = Furniture.objects.all().order_by('id')
    serializer_class = FurnitureSerializer

class FurnitureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all().order_by('id')
    serializer_class = FurnitureSerializer

@api_view(['GET'])
def getUserProfile (request):
    user = request.user #this will require a token provided when log in to return user data, different from the user data we can get by solely look up using admin pannel
    serializer = UserSerializer(user, many = False)
    return Response (serializer.data)

Skip to content
Search or jump to…
Pulls
Issues
Marketplace
Explore

@carablythe
carablythe
/
furniture_backend
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
More
furniture_backend/furnitures_api/views.py /

Victoria Le Cart model added
Latest commit a74e62e 5 hours ago
 History
 1 contributor
74 lines (54 sloc)  2.96 KB

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import FurnitureSerializer, CartSerializer, UserSerializer, UserSerializerWithToken
from .models import Furniture, Cart
from django.contrib.auth.models  import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
#serialize token, this is from simple jwt documentation

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.hashers import make_password
#This is used to hash the pw before we can store it in our database

class FurnitureList(generics.ListCreateAPIView):
    queryset = Furniture.objects.all().order_by('id')
    serializer_class = FurnitureSerializer

class FurnitureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all().order_by('id')
    serializer_class = FurnitureSerializer



class ReviewList(generics.ListCreateAPIView):
        queryset = Review.objects.all().order_by('id')
        serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Review.objects.all().order_by('id')
        serializer_class = ReviewSerializer


########Cart Serializer######
class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all().order_by('id')
    serializer_class =  CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer


#########This Section is to create/obtain User profile#############
@api_view(['POST'])
def registerUser (request):
    data = request.data
    user = User.objects.create (
        first_name = data['name'],
        username = data['email'],
        email = data['email'],
        password = make_password(data['password'])
    )
    serializer = UserSerializerWithToken(user, many = False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile (request):
    user = request.user #this will require a token provided when log in to return user data, different from the user data we can get by solely look up using admin pannel
    serializer = UserSerializer(user, many = False)
    return Response (serializer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate (self, attrs): #we overide the validate method and serialize the user data, so that when we work with the frontend we dont have to decode the return json information, instead we have the username and email easy to reach
        data = super().validate(attrs)

        serializer = UserSerializerWithToken (self.user).data

        for k,v in serializer.items (): #for every key, value pair - data of [k]ey equal [v]alue. We can also write them all out data['email'] = somemail@email.com, etc... but this way the expression can be more systematic and more dry
            data[k] = v


        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer #the serializer class will actually return back the user data
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete

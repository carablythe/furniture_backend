# The serializer will the take the data in database and convert it into JSON
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Furniture, Cart
# , Review
from rest_framework_simplejwt.tokens import RefreshToken


class FurnitureSerializer(serializers.ModelSerializer): #tells django to convert sql to JSON
    class Meta:
        model = Furniture #tells django which model to use
        fields = ('id','name','img','imgURL','color','category','price','quantity','availability','rating') #tells django which fields to include


class CartSerializer(serializers.ModelSerializer): #tells django to convert sql to JSON
    class Meta:
        model = Cart #tells django which model to use
        fields = ('id','user','product','qty','price','img',)



class UserSerializer(serializers.ModelSerializer): #tells django to convert sql to JSON
    class Meta:
        model = User #tells django which model to use
        fields = ('id','username','email','first_name','is_staff',) #tells django to include all fields

class UserSerializerWithToken(UserSerializer):
    token  = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ('id','username','email','first_name','is_staff','token',)

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)


# class ReviewSerializer(serializers.ModelSerializer): #tells django to convert sql to JSON
#     class Meta:
#         model = Review #tells django which model to use
#         fields = ('id', 'product', 'user', 'rating',) #tells django to include all fields

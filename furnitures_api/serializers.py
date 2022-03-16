# The serializer will the take the data in database and convert it into JSON
from rest_framework import serializers
from .models import Furniture

class FurnitureSerializer(serializers.ModelSerializer): #tells django to convert sql to JSON
    class Meta:
        model = Furniture #tells django which model to use
        fields = ('id','name','img','color','category','price','quantity','availability',) #tells django which fields to include

from rest_framework import serializers
from .models import Furniture, Cart, Review

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

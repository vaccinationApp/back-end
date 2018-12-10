from rest_framework import serializers
from .models import Suit,TypesofLiveStock,LiveStock,Sex


class SuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suit
        fields = ('id', 'name')

class LiveStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStock
        fields = ('id','sex','age','typeoflivestock','farmer','placeofbirth')

class TypesofLiveStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesofLiveStock
        fields = ('id','name','suit')

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ('id','name')


from rest_framework import serializers

from vaccination.serializers import VaccinationSerializer
from .models import Suit,TypesofLiveStock,LiveStock,Sex


class SuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suit
        fields = ('id', 'name')

class LiveStockSerializer(serializers.ModelSerializer):
    vaccinations = serializers.SerializerMethodField()
    class Meta:
        model = LiveStock
        fields = ('id','sex','age','typeoflivestock','farmer','placeofbirth', 'vaccinations')

    def get_vaccinations(self, instance):
        serializer = VaccinationSerializer(instance.vaccination_set.all(), many=True)
        return serializer.data


class TypesofLiveStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesofLiveStock
        fields = ('id','name','suit')

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ('id','name')



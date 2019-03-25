from rest_framework import serializers

from livestock.serializers import LiveStockSerializer
from .models import Farmer,Village,Region,Oblast,Country,RuralDistrict


class FarmerSerializer(serializers.ModelSerializer):
    livestocks = serializers.SerializerMethodField()

    class Meta:
        model = Farmer
        fields = ('id', 'name', 'phone', 'email','address','coordinate','village', 'livestocks')

    def get_livestocks(self, instance):
        serializer = LiveStockSerializer(instance.livestocks.all(), many=True)
        return serializer.data
class TableFarmerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farmer
        fields = ('id', 'name', 'phone', 'email','address','coordinate','village', 'livestocks')
        depth = 3

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ('id','name','ruraldistrict')

class RuralDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuralDistrict
        fields = ('id','name','region')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name','oblast')

class OblastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oblast
        fields = ('id', 'name','country')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name')



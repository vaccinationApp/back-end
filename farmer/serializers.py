from rest_framework import serializers
from .models import Farmer,Village,Region,Oblast,Country,RuralDistrict


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'name', 'phone', 'email','address','coordinate','village')

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



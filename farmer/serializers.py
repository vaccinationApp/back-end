from rest_framework import serializers
from .models import Farmer,Village,Region,Oblast,Country,RuralDistrict


class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'name', 'phone', 'email','address','coordinate','village')

class VillageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Village
        fields = ('id','name','ruraldistrict')

class RuralDistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RuralDistrict
        fields = ('id','name','region')

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name','oblast')

class OblastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oblast
        fields = ('id', 'name','country')

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name')



from rest_framework import serializers
from .models import Disease,Bloodtest,Medicine,Vaccination,Modeofapplication


class ModeofapplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modeofapplication
        fields = ('id', 'name')
class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disease
        fields = ('id', 'name')

class BloodtestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bloodtest
        fields = ('id', 'status','date')

class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id','name','dose','disease','modeofapplication','typesoflivestock','description')

class VaccinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccination
        fields = ('id','employee','livestock','medicine','bloodtest','date')


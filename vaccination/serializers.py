from rest_framework import serializers
from .models import Disease,Bloodtest,Medicine,Vaccination,Modeofapplication,TestMethod


class ModeofapplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modeofapplication
        fields = ('id', 'name')
class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('id', 'name')

class TestMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestMethod
        fields = ('id','name')

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id','name','volume','dose','disease','modeofapplication','typesoflivestock','description')

class BloodtestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloodtest
        fields = ('id','livestock','employee','disease','testmethod','status','date')

class TableVaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = ('id','employee','livestock','medicine','date')
        depth = 3

class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = ('id', 'employee', 'livestock', 'medicine', 'date')


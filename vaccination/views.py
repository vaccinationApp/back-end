# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Disease,Medicine,Bloodtest,Vaccination,Modeofapplication,TestMethod
from .serializers import DiseaseSerializer,MedicineSerializer,VaccinationSerializer,BloodtestSerializer,ModeofapplicationSerializer,TestMethodSerializer
class DiseaseView(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class MedicineView(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class TestMethodView(viewsets.ModelViewSet):
    queryset = TestMethod.objects.all()
    serializer_class = TestMethodSerializer

class BloodtestView(viewsets.ModelViewSet):
    queryset = Bloodtest.objects.all()
    serializer_class = BloodtestSerializer

class VaccinationView(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer

class ModeofapplicationView(viewsets.ModelViewSet):
    queryset = Modeofapplication.objects.all()
    serializer_class = ModeofapplicationSerializer
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from django.shortcuts import render

# Create your views here.
from django_filters import filters
from rest_framework import viewsets
from .models import Disease,Medicine,Bloodtest,Vaccination,Modeofapplication,TestMethod
from .serializers import DiseaseSerializer,MedicineSerializer,VaccinationSerializer,BloodtestSerializer,ModeofapplicationSerializer,TestMethodSerializer,TableVaccinationSerializer
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

class VacDateFilter(django_filters.FilterSet):
    start_date = filters.DateFilter(field_name='date',lookup_expr=('gt'),)
    end_date = filters.DateFilter(field_name='date',lookup_expr=('lt'))
    #date_range = DateRangeFilter(name='date')
    class Meta:
        model = Vaccination
        fields = ['employee','livestock__farmer__name','livestock']

class VaccinationView(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer


class TableVaccinationView(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = TableVaccinationSerializer
    filter_class = VacDateFilter

class ModeofapplicationView(viewsets.ModelViewSet):
    queryset = Modeofapplication.objects.all()
    serializer_class = ModeofapplicationSerializer
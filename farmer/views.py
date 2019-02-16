# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions
from rest_framework import filters

from .models import Farmer,Village,Region,Oblast,Country,RuralDistrict
from .serializers import FarmerSerializer, VillageSerializer, RegionSerializer, OblastSerializer, CountrySerializer, RuralDistrictSerializer


class FarmerView(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
   # search_fields = ('name', 'id')


class VillageView(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

class RuralDistrictView(viewsets.ModelViewSet):
    queryset = RuralDistrict.objects.all()
    serializer_class = RuralDistrictSerializer

class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class OblastView(viewsets.ModelViewSet):
    queryset = Oblast.objects.all()
    serializer_class = OblastSerializer

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

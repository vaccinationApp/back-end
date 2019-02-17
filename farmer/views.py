# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions, status
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Farmer,Village,Region,Oblast,Country,RuralDistrict
from .serializers import FarmerSerializer, VillageSerializer, RegionSerializer, OblastSerializer, CountrySerializer, RuralDistrictSerializer


class VacDateFilter(django_filters.FilterSet):
    start_date = filters.DateFilter(field_name='livestocks__vaccination__date',lookup_expr=('gt'),)
    end_date = filters.DateFilter(field_name='livestocks__vaccination__date',lookup_expr=('lt'))
    #date_range = DateRangeFilter(name='date')
    class Meta:
        model = Farmer
        fields = ['name','id']
class FarmerView(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
   # filter_backends = (filters.DjangoFilterBackend,)
    #search_fields = ('name', 'id')
    #filterset_fields = ('id','name','livestocks__vaccination__date')
    filter_class = VacDateFilter


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


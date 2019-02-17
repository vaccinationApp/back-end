# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions, status
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Farmer,Village,Region,Oblast,Country,RuralDistrict
from .serializers import FarmerSerializer, VillageSerializer, RegionSerializer, OblastSerializer, CountrySerializer, RuralDistrictSerializer

#class StandardResultsSetPagination(PageNumberPagination):
 #   page_size = 100
    #page_size_query_param = 'page_size'
    #max_page_size = 10000


class FarmerView(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    #search_fields = ('name', 'id')
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Farmer.objects.all().order_by('id'))

        page = request.GET.get('page')

        try:
            page = self.paginate_queryset(queryset)
        except Exception as e:
            page = []
            data = page
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": 'No more record.',
                "data": data
            })

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(data)

        # serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": 'Sitting records.',
        })

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


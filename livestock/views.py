# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import TypesofLiveStock,LiveStock,Sex,Suit
from .serializers import TypesofLiveStockSerializer,LiveStockSerializer,SexSerializer,SuitSerializer
class SexView(viewsets.ModelViewSet):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class SuitView(viewsets.ModelViewSet):
    queryset = Suit.objects.all()
    serializer_class = SuitSerializer

class LiveStockView(viewsets.ModelViewSet):
    queryset = LiveStock.objects.all()
    serializer_class = LiveStockSerializer

class TypesofLiveStockView(viewsets.ModelViewSet):
    queryset = TypesofLiveStock.objects.all()
    serializer_class = TypesofLiveStockSerializer


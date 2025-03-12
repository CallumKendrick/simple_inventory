from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
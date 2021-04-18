from django.shortcuts import render
from django.contrib.auth.models import User
from public_view.models import Property, PropertyType, Location
from rest_framework import viewsets
from .seriallizers import PropertySerializer, LocationSerializer, PropertyTypeSerializer


class PropertyView(viewsets.ModelViewSet):
	queryset = Property.objects.all()
	serializer_class = PropertySerializer

class LocationView(viewsets.ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class PropertyTypeView(viewsets.ModelViewSet):
	queryset = PropertyType.objects.all()
	serializer_class = PropertyTypeSerializer
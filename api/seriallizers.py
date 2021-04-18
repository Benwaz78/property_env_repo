from django.contrib.auth.models import User
from public_view.models import Property, Location, PropertyType
from rest_framework import serializers

class PropertySerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model = Property
		fields = ('id', 'property_name', 'property_img1', 'prize', 'rooms')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model = Location
		fields = ('id', 'name',)

class PropertyTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model = PropertyType
		fields = ('id', 'name', 'description')
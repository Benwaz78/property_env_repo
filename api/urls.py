
from django.urls import path, include
from api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('properties', views.PropertyView)
router.register('locations', views.LocationView)
router.register('propertytype', views.PropertyTypeView)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]

# # Create your views here.
import json
from rest_framework import viewsets
from .models import Provider, Jeojson
from .serializers import ProviderSerializer, JeojsonSerializer
from . import serializers
from django_filters import rest_framework as filters


class ProviderViewset(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


class JeojsonViewset(viewsets.ModelViewSet):
    queryset = Jeojson.objects.all()
    serializer_class = serializers.JeojsonSerializer


    def get_queryset(self):
        queryset = super().get_queryset()
        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)
        if lat == None or lng == None:
            return queryset
        lat = int(lat)
        lng = int(lng)
        polygons = []
        for polygon in queryset:
            jeojson = polygon.jeojson
            flag = False
            if isinstance(jeojson, str) == True:
                jeojson = json.loads(polygon.jeojson)
            for obj in jeojson:
                if obj['lat'] == lat and obj['lng']== lng:
                    flag = True
            if flag == True:
                polygons.append(polygon)
        return polygons

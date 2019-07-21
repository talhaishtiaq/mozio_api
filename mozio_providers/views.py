
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
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('lat_lng')
    # 
    # def get_queryset(self):
    #     queryset = Jeojson.objects.all()
    #     lat_lng = self.request.query_params.get('lat_lng')
    #     print(json.loads(lat_lng))
    #     if lat_lng:
    #         filter_backends = (filters.DjangoFilterBackend,)
    #         filter_fields = ('jeojson',lat_lng)
    #     return queryset

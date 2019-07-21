# mozio_providers/serializers
from rest_framework import serializers
from .models import Provider, Jeojson


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone_number',
                  'language', 'currency' )

class JeojsonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jeojson
        fields = ('id', 'provider_id', 'name', 'price',
                  'jeojson' )

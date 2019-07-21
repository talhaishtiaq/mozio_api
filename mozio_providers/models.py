from jsonfield import JSONField
from django.db import models

# Create your models here.
class Provider(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(default='name@email.com')
    phone_number = models.CharField(max_length=100, default='0000000')
    language = models.CharField(max_length=50, default='English')
    currency = models.CharField(max_length=50, default='USD')

class Jeojson(models.Model):

    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100, default='1000')
    jeojson = JSONField(default="{ 'key': 'value'}")

import json
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from .views import ProviderViewset
from .models import Provider

class Tests(APITestCase):
    client = APIClient()
    url = 'http://127.0.0.1:8000/api/v1'

    def test_create_provider(self):
        response = self.client.post(self.url+'/providers/', {'name': 'provider1'})
        self.assertEqual(201, response.status_code)
    def test_create_jeojson(self):
        response = self.client.post(self.url+'/providers/', {'name': 'provider1'})
        response = self.client.post(self.url+'/jeojsons/', {'name': 'jeojson1','provider_id':1})
        self.assertEqual(201, response.status_code)

    def test_read_provider(self):
        response = self.client.post(self.url+'/providers/', {'name': 'provider1'})
        response = self.client.get(self.url+'/providers/')
        self.assertEqual(200, response.status_code)
    def test_read_jeojson(self):
        response = self.client.post(self.url+'/providers/', {'name': 'provider1'})
        response = self.client.post(self.url+'/jeojsons/', {'name': 'jeojson1','provider_id':1})
        response = self.client.get(self.url+'/jeojsons/')
        self.assertEqual(200, response.status_code)

    def test_update_provider(self):
        response = self.client.post(self.url+'/providers/', {"name": "provider1"})
        response = self.client.put(self.url+'/providers/1/', {"name": "provider234556"})
        response_data = json.loads(response.content)
        self.assertEqual(response_data["name"], 'provider234556')

    def test_update_jeojson(self):
        response = self.client.post(self.url+'/providers/', {'name': 'provider1'})
        response = self.client.post(self.url+'/jeojsons/', {'name': 'jeojson1','provider_id':1})
        response = self.client.put(self.url+'/jeojsons/1/', {"name": "jeojson12345", 'provider_id':1})
        response_data = json.loads(response.content)
        print(response_data)
        self.assertEqual(response_data.get("name"), 'jeojson12345')

    def test_delete_provider(self):
        response = self.client.post(self.url+'/providers/', {"name": "provider1"})
        response = self.client.delete(self.url+'/providers/1/')
        self.assertEqual(204, response.status_code)

    def test_delete_jeojson(self):
        response = self.client.post(self.url+'/providers/', {'name': 'provider1'})
        response = self.client.post(self.url+'/jeojsons/', {'name': 'jeojson1','provider_id':1})
        response = self.client.delete(self.url+'/jeojsons/1/')
        self.assertEqual(204, response.status_code)

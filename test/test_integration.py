# test_integration.py

from django.test import TestCase, factory
from django.urls import reverse
from case_project.models import Device, LocationHistory
from unittest.mock import patch
from rest_framework.test import APIRequestFactory

class DeviceIntegrationTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    @patch('app.views.Device.objects')
    def test_create_device_integration(self, mock_device_objects):
        mock_device_objects.create.return_value = Device(id=1, name="Test Device")
        response = self.factory.post(reverse('create_device'), {'name': 'Test Device'})
        self.assertEqual(response.status_code, 200)

    @patch('app.views.Device.objects')
    def test_add_location_integration(self, mock_device_objects):
        mock_device_objects.filter.return_value.first.return_value = None
        response = self.factory.post(reverse('add_location', kwargs={'device_id': 1}), {'latitude': 123.456, 'longitude': 78.90})
        self.assertEqual(response.status_code, 404) 

    @patch('app.views.Device.objects')
    def test_delete_device_integration(self, mock_device_objects):
        mock_device_objects.filter.return_value.first.return_value = None
        response = self.factory.delete(reverse('delete_device', kwargs={'device_id': 1}))
        self.assertEqual(response.status_code, 404)  

    @patch('app.views.Device.objects')
    def test_list_devices_integration(self, mock_device_objects):
        mock_device_objects.all.return_value = [Device(id=1, name="Test Device")]
        response = self.factory.get(reverse('list_devices'))
        self.assertEqual(response.status_code, 200)

    @patch('app.views.Device.objects')
    @patch('app.views.LocationHistory.objects')
    def test_list_location_history_integration(self, mock_location_objects, mock_device_objects):
        mock_device_objects.filter.return_value.first.return_value = None
        response = self.factory.get(reverse('list_location_history', kwargs={'device_id': 1}))
        self.assertEqual(response.status_code, 404) 

    @patch('app.views.Device.objects')
    @patch('app.views.LocationHistory.objects')
    def test_get_last_location_for_all_devices_integration(self, mock_location_objects, mock_device_objects):
        mock_device_objects.all.return_value = [Device(id=1)]
        mock_location_objects.order_by.return_value.first.return_value = LocationHistory(latitude=123.456, longitude=78.90)
        response = self.factory.get(reverse('get_last_location_for_all_devices'))
        self.assertEqual(response.status_code, 200)

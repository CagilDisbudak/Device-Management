from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

class DeviceViewsTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_device(self):
        response = self.factory.post(('create_device'), {'name': 'Test Device'})
        self.assertEqual(response.status_code, 200)

    def test_add_location(self):
        response = self.factory.post(reverse('add_location', kwargs={'device_id': 1}), {'latitude': 123.456, 'longitude': 78.90})
        self.assertEqual(response.status_code, 404)  # Assuming device with ID 1 doesn't exist

    def test_delete_device(self):
        response = self.factory.delete('delete_device', kwargs={'device_id': 1})
        self.assertEqual(response.status_code, 404)  # Assuming device with ID 1 doesn't exist

    def test_list_devices(self):
        response = self.factory.get('list_devices')
        self.assertEqual(response.status_code, 200)

    def test_list_location_history(self):
        response = self.factory.get('list_location_history', kwargs={'device_id': 1})
        self.assertEqual(response.status_code, 404)  # Assuming device with ID 1 doesn't exist

    def test_get_last_location_for_all_devices(self):
        response = self.factory.get('get_last_location_for_all_devices')
        self.assertEqual(response.status_code, 200)

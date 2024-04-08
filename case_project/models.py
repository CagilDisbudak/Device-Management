from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)


class LocationHistory(models.Model):
    device = models.ForeignKey(Device, related_name='location_history', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
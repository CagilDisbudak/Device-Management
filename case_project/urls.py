from django.urls import path
from . import views

urlpatterns = [
    path('devices/create/', views.create_device),
    path('devices/<int:device_id>/delete/', views.delete_device),
    path('devices/list/', views.list_devices),
    path('devices/<int:device_id>/location/history/', views.list_location_history),
    path('devices/location/last/', views.get_last_location_for_all_devices),
]
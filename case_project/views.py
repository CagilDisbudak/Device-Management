from fastapi import FastAPI, HTTPException
from case_project.models import Device, LocationHistory
from case_project.serializers import LocationHistorySerializer, DeviceSerializer
from case_project.post_task import process_location_data
from pydantic import BaseModel


app = FastAPI()

class DeviceCreate(BaseModel):
    name: str

@app.post("/devices/create/")
def create_device(device_data: DeviceCreate):
    new_device = Device.objects.create(name=device_data.name)
    return {"id": new_device.id, "name": new_device.name}

# @app.post("/devices/{device_id}/add_location/")
# def add_location(device_id: int, location_data: LocationHistorySerializer):
#     device = Device.objects.filter(id=device_id).first()
#     if not device:
#         raise HTTPException(status_code=404, detail="Device not found")

#     serialized_data = location_data.dict()

#     process_location_data.delay([serialized_data])

#     return {"message": "Location data added to queue"}

@app.delete("/devices/{device_id}/delete/")
def delete_device(device_id: int):
    device = Device.objects.filter(id=device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    device.delete()
    return {"message": "Device deleted successfully"}

@app.get("/devices/list/")
def list_devices():
    devices = Device.objects.all()
    return devices

@app.get("/devices/{device_id}/location/history/")
def list_location_history(device_id: int):
    device = Device.objects.filter(id=device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    history = device.location_history.all()
    return history

@app.get("/devices/location/last/")
def get_last_location_for_all_devices():
    devices = Device.objects.all()
    last_locations = []
    for device in devices:
        last_location = device.location_history.order_by('-timestamp').first()
        last_locations.append({"device_id": device.id, "latitude": last_location.latitude, "longitude": last_location.longitude})
    return last_locations

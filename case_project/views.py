import json
import logging
from django.http import JsonResponse
from fastapi import FastAPI, HTTPException, Request
from case_project.models import Device
from case_project.post_task import process_location_data


app = FastAPI()


@app.post("/devices/create/")
def create_device(request: Request):
    if not request.body:
        return JsonResponse({"error": "Empty request body"}, status=400)
    try:
        device_data_utf = request.body.decode('utf-8')
        device_data = json.loads(device_data_utf)
        new_device = Device.objects.create(name=device_data['name'])
        logging.info(f"Created device: {new_device.id}, Name: {new_device.name}")
        return {"id": new_device.id, "name": new_device.name}
    except json.decoder.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)


@app.post("/devices/{device_id}/add_location/", response_model=None)
def add_location(request: Request, device_id: int):
    location_data_utf = request.body.decode()
    location_data = json.loads(location_data_utf)
    device = Device.objects.filter(id=device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    process_location_data.delay([location_data])
    logging.info(f"Added location for device {device_id}: {location_data}")


@app.delete("/devices/{device_id}/delete/")
def delete_device(device_id: int):
    device = Device.objects.filter(id=device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    device.delete()
    logging.info(f"Deleted device: {device_id}")
    return {"message": "Device deleted successfully"}


@app.get("/devices/list/")
def list_devices():
    devices = Device.objects.all()
    logging.info("Listed all devices")
    return devices


@app.get("/devices/{device_id}/location/history/")
def list_location_history(device_id: int):
    device = Device.objects.filter(id=device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    history = device.location_history.all()
    logging.info(f"Listed location history for device {device_id}")
    return history


@app.get("/devices/location/last/")
def get_last_location_for_all_devices():
    devices = Device.objects.all()
    last_locations = []
    for device in devices:
        last_location = device.location_history.order_by('-timestamp').first()
        last_locations.append(
            {"device_id": device.id, "latitude": last_location.latitude, "longitude": last_location.longitude})
        logging.info(f"Retrieved last location for device {device.id}")
    return last_locations

# Device Management API Documentation

## Overview

This API provides endpoints for managing devices and their locations. It allows creating, listing, and deleting devices, as well as adding and retrieving location history for devices.

## Base URL

The base URL for accessing the API endpoints is:
http://localhost:8000


## Authentication

Authentication is not implemented in this version of the API. All endpoints are publicly accessible.

## Error Handling

The API follows RESTful principles for error handling. When an error occurs, the API returns an appropriate HTTP status code along with a JSON response containing a `detail` field describing the error.

### Error Responses

- **404 Not Found**: Returned when a requested resource (e.g., device) is not found.
- **422 Unprocessable Entity**: Returned when the request body is invalid (e.g., missing required fields).
- **500 Internal Server Error**: Returned for unexpected server errors.

## Endpoints

### Create Device

- **URL**: `/devices/create/`
- **Method**: `POST`
- **Description**: Create a new device with a given name.
- **Request Body**:
  - `name` (string, required): The name of the device.
- **Success Response**:
  - **Code**: 200
  - **Content**: JSON object containing the `id` and `name` of the created device.
- **Error Response**:
  - **Code**: 422 Unprocessable Entity
  - **Content**: JSON object with details about the validation error(s).

### Add Location

- **URL**: `/devices/{device_id}/add_location/`
- **Method**: `POST`
- **Description**: Add a new location to the history of a device.
- **URL Parameters**:
  - `device_id` (integer, required): The ID of the device.
- **Request Body**:
  - Location data (structure/format not specified).
- **Success Response**:
  - **Code**: 200
  - **Content**: None
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**: JSON object with a message indicating that the device was not found.

### Delete Device

- **URL**: `/devices/{device_id}/delete/`
- **Method**: `DELETE`
- **Description**: Delete a device by its ID.
- **URL Parameters**:
  - `device_id` (integer, required): The ID of the device to delete.
- **Success Response**:
  - **Code**: 200
  - **Content**: JSON object with a message indicating successful deletion.
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**: JSON object with a message indicating that the device was not found.

### List Devices

- **URL**: `/devices/list/`
- **Method**: `GET`
- **Description**: Retrieve a list of all devices.
- **Success Response**:
  - **Code**: 200
  - **Content**: JSON array containing details of all devices.
- **Error Response**: None

### List Location History

- **URL**: `/devices/{device_id}/location/history/`
- **Method**: `GET`
- **Description**: Retrieve the location history for a specific device.
- **URL Parameters**:
  - `device_id` (integer, required): The ID of the device.
- **Success Response**:
  - **Code**: 200
  - **Content**: JSON array containing location history entries for the device.
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**: JSON object with a message indicating that the device was not found.

### Get Last Location for All Devices

- **URL**: `/devices/location/last/`
- **Method**: `GET`
- **Description**: Retrieve the last known location for all devices.
- **Success Response**:
  - **Code**: 200
  - **Content**: JSON array containing the last known locations of all devices.
- **Error Response**: None

## Example Usage

### Create Device

```http
POST /devices/create/
Content-Type: application/json

{
    "name": "MyDevice"
} 

```


### Add Location

```http
POST /devices/{device_id}/add_location/
Content-Type: application/json

{
    "latitude": 123.456,
    "longitude": 789.012
}
```

### Delete Device

```
DELETE /devices/{device_id}/delete/
```

### List Devices
```
GET /devices/list/
```

### List Location History 
 
```
GET /devices/{device_id}/location/history/
```

### Get Last Location for All Devices

```
GET /devices/location/last/
```

# WASTEWISE API 2023

This repository contains APIs for the Wastewise team's capstone project, these APIs connect the machine learning model to the front end

### API Endpoint: "/"
This endpoint will return a welcome json.

### API Endpoint: "/predict"
This endpoint is used to perform image detection using the POST method.


## Example:
### Request

**Header:**
- Content-Type: multipart/form-data

**Body:**
- Use the POST method and include the image file with the key name 'file'.

**Example of Use with cURL:**
```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@path/to/your/image.jpg" your-api//predict

# WASTEWISE API 2023

This repository contains APIs for the Wastewise team's capstone project, these APIs connect the machine learning model to the front end


## API Endpoint: /predict
This endpoint is used to perform image detection using the POST method.


###Example:

### Request

**Header:**
- Content-Type: application/json

**Body:**
```json
{
  "image": "base64_encoded_image"
}

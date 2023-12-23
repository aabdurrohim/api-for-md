# WASTEWISE API 2023

This repository contains APIs for the Wastewise team's capstone project, these APIs connect the machine learning model to the front end


## API Endpoint: /predict
This endpoint is used to perform image detection using the POST method.


###Example:
### Request

**Header:**
- Content-Type: multipart/form-data

**Body:**
- Gunakan metode POST dan sertakan file gambar dengan nama kunci 'file'.

**Contoh Penggunaan dengan cURL:**
```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@path/to/your/image.jpg" http://url-api-anda/predict

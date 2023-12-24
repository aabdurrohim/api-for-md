
# WASTEWISE 2023

Welcome to WasteWise Prediction API! This API is designed to predict the type of waste (e.g., cardboard, glass, plastic) based on an image using a pre-trained deep learning model.

# API Endpoints
## Home
### Endpoint: /
### Method: GET
### Description: Get a welcome message.


## Making Predictions
Use the /predict endpoint to make waste type predictions based on an image. Send a POST request with the image file to get predictions.

#### POST

```http
  POST /api/predict
```

WasteWise API
Introduction
Welcome to the WasteWise API, an endpoint that facilitates waste classification predictions based on images. This API is designed to be used by mobile developers to integrate waste classification capabilities into their applications.

Getting Started
Prerequisites
Python (3.x recommended)
Flask
Keras
PIL (Pillow)
Install the required Python packages using the following command:

bash
Copy code
pip install flask keras Pillow
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/WasteWise.git
cd WasteWise
Run the Flask app:
bash
Copy code
python main.py
The API should be running on http://localhost:5000.

API Endpoints
1. Welcome Message
Endpoint: /

Method: GET

Description: Retrieve a welcome message.

Example:

bash
Copy code
curl http://localhost:5000/
Response:

json
Copy code
{
  "Message": "Welcome to WasteWise"
}
2. Image Prediction
Endpoint: /predict

Method: POST

Description: Upload an image for waste classification prediction.

Example:

bash
Copy code
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@path/to/your/image.jpg" http://localhost:5000/predict
Response:

json
Copy code
{
  "prediction": "cardboard",
  "probability": 0.92
}
Mobile Integration
To integrate the API into your mobile application:

Fetch Welcome Message:

Make a GET request to the / endpoint to receive the welcome message.
Predict Image:

Capture an image using the device's camera.
Send a POST request to the /predict endpoint with the image file for waste classification prediction.
bash
Copy code
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@path/to/your/image.jpg" http://localhost:5000/predict
Receive the prediction results in the response.

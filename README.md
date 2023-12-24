# WasteWise 2023 API

Welcome to WasteWise Prediction API! This API is designed to predict the type of waste (e.g., cardboard, glass, plastic) based on an image using a pre-trained deep learning model.

## API Endpoints

### Home

- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Get a welcome message.
- **Example Request:**

  ```bash
  curl http://127.0.0.1:5000/
  ```
- **Example Responses:**
  ```bash
  {
  "Message": "Welcome to WasteWise"
  }
  ```
### Predict

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** Upload an image file for waste prediction.
- **Example Request:**

  ```bash
  curl -X POST -F "file=@path/to/image.jpg" http://127.0.0.1:5000/api/predict
- **Example Responses:**
  ```bash
  {
  "prediction": "paper",
  "probability": 0.987
  }
  ```


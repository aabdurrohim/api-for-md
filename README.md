
# WASTEWISE 2023

Welcome to WasteWise Prediction API! This API is designed to predict the type of waste (e.g., cardboard, glass, plastic) based on an image using a pre-trained deep learning model.

## API ENDPOINTS

### HOME
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

## Making Predictions
Use the /predict endpoint to make waste type predictions based on an image. Send a POST request with the image file to get predictions.

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** Upload an image file for waste prediction.
- **Example Request:**

| Key | Type     | Value               |
| :-------- | :------- | :------------------------- |
| `file` | `file` | Upload Image file for prediction |




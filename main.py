from flask import Flask, request, jsonify
from model.predict import perform_prediction

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return {"Message":"Welcome to WasteWise"}

@app.route('/predict', methods=['POST'])
def predict_image():
    try:
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return jsonify({"error": "No file part"})

        file = request.files['file']

        # If the user does not select a file, browser also submits an empty part without filename
        if file.filename == '':
            return jsonify({"error": "No selected file"})

        # Perform prediction
        class_label_prediction, probability = perform_prediction(file)

        # Return the prediction result
        return jsonify({"prediction": class_label_prediction, "probability": probability})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

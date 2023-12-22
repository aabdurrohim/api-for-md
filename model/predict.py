from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename
from flask import jsonify

model_path = "model/model_WasteWise_baru80.h5"
class_labels = ['battery', 'cardboard', 'carton', 'glass', 'metal', 'organic', 'paper', 'plastic']

def preprocess_image(img):
    # Load and preprocess the image
    img = img.convert('RGB')
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values to between 0 and 1
    return img_array

def perform_prediction(file):
    try:
        # Read and preprocess the uploaded image directly
        img = Image.open(file)
        img_array = preprocess_image(img)

        # Load the model
        model = load_model(model_path)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        # Perform prediction
        prediction = model.predict(img_array, batch_size=10)
        class_index = np.argmax(prediction, axis=1)
        class_label_prediction = class_labels[class_index[0]]
        probability = float(prediction[0][class_index[0]])

        return class_label_prediction, probability

    except Exception as e:
        raise e

import tensorflow.keras
import numpy as np
import cv2
import sys
import json,codecs

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('C:/xampp/htdocs/ML_Based_Skin_Cancer_Identification_Web/PHP/SkinCancer_CNN.h5')
model_ResNet50 = tensorflow.keras.models.load_model('C:/xampp/htdocs/ML_Based_Skin_Cancer_Identification_Web/PHP/SkinCancer_CNN_ResNet50.h5')
model_VGG16 = tensorflow.keras.models.load_model('C:/xampp/htdocs/ML_Based_Skin_Cancer_Identification_Web/PHP/SkinCancer_CNN_VGG16.h5')

def detection(filename):
    # print(filename)
    image_size = 128

    img = cv2.imread("C:/xampp/htdocs/ML_Based_Skin_Cancer_Identification_Web/PHP/uploads/"+filename)

    if img is None:
        print(f"Error loading image: {filename}")

    img = cv2.resize(img, (image_size, image_size))
    img = img / 255.0
    prediction = model.predict(np.array([img]))
    prediction_ResNet50 = model_ResNet50.predict(np.array([img]))
    prediction_VGG16 = model_VGG16.predict(np.array([img]))

    # print(prediction)
    json.dump([prediction.tolist(),prediction_ResNet50.tolist(),prediction_VGG16.tolist()], codecs.open("result.json", 'w', encoding='utf-8'),
              separators=(',', ':'),
              indent=4)

if __name__ == '__main__':
    detection(str(sys.argv[1]))


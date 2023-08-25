import tensorflow.keras
import numpy as np
import cv2
import sys
import json,codecs

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('C:/xampp/htdocs/ML_Based_Skin_Cancer_Identification_Web/PHP/SkinCancer_CNN.h5')

def detection(filename):
    # print(filename)
    image_size = 32

    img = cv2.imread("C:/xampp/htdocs/ML_Based_Skin_Cancer_Identification_Web/PHP/uploads/"+filename)

    if img is None:
        print(f"Error loading image: {filename}")

    img = cv2.resize(img, (image_size, image_size))
    img = img / 255.0
    prediction = model.predict(np.array([img]))

    # print(prediction)
    json.dump(prediction.tolist(), codecs.open("result.json", 'w', encoding='utf-8'),
              separators=(',', ':'),
              sort_keys=True,
              indent=4)

if __name__ == '__main__':
    detection(str(sys.argv[1]))


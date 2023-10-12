import tensorflow as tf
import cv2
import numpy as np
import json

model = tf.keras.models.load_model('model/model.h5')

with open('model/encoder.json', 'r') as f:
    label_encode_inverse = json.load(f)

def image_to_numpy(loc):
    image = cv2.imread(loc)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (128, 128))
    image = image.reshape(1, 128, 128, 1)
    return image

def prediction(loc):
    image = image_to_numpy(loc)
    index = np.argmax(model.predict(image))
    return label_encode_inverse[str(index)]
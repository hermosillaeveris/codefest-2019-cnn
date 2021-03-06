import os
import re

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

animal_model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'ml_ia/animals_mnist.h5'))

dirname = os.path.join(os.getcwd(), 'static/test')
imgpath = dirname + os.sep

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

def predict(imageUrl):
    filepath = os.path.join(dirname, imageUrl)
    images = []
    image = plt.imread(filepath)
    images.append(image)
    X = np.array(images, dtype=np.uint8) #convierto de lista a numpy
    real_X = X.astype('float32')
    real_X = real_X / 255.0
    predictions = animal_model.predict(real_X)
    predict = []
    for i in range(len(predictions[0])):
      predict.append({ 'name': class_names[i], 'value': str(predictions[0][i]) })
    return predict

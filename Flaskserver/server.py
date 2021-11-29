# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:17:09 2021

@author: jglob
"""

import tensorflow as tf 
import numpy as np
from keras.preprocessing import image
import warnings 
import base64

warnings.filterwarnings('ignore')

model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 300x300 with 3 bytes color
    # This is the first convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(600, 600, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # The second convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The third convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fourth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fifth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
     tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(300, activation='relu'),
    # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('horses') and 1 for the other ('humans')
    tf.keras.layers.Dense(5, activation='softmax')
])

model.load_weights('../model_weights/simple_images')

dic_champions = {0:'Aatrox',1:'Ahri',2:'Akali',3:'Anivia',4:'Cassiopeia'}

url = 'C:/Users/jglob/Music/New_projects/LeagueOfLegendsChampionClassifier/simple_images/Cassiopeia_lol/Cassiopeia lol_9.jpeg'
def make_prediction(img_encoded):
    
    imgdata = base64.b64decode(img_encoded)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    img = image.load_img(filename, target_size=(600, 600))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    prediction = np.flip(np.argsort(model.predict(x)))[0][0]
    return {'champion':dic_champions[prediction]}


import pandas as pd 
import numpy as np 
import tensorflow as tf
import matplotlib.pyplot as plt 
import os

def scheduler(epoch):
    if epoch<= WARMUP_EPOCH:
        lr = INITIAL_LEARNINGRATE *epoch/WARMUP_EPOCH
    else:
        lr = INITIAL_LEARNINGRATE * DECAY_RATE**(epoch-WARMUP_EPOCH)
    return lr

def BuildModel(num_class, img_size):
    print('--------------Building The Model...--------------')
    base_model = tf.keras.applications.Xception(include_top = False,
                                                weights = 'imagenet',
                                                input_shape = (img_size, img_size, 3))
    base_model.trainable = True
    print("\nNumber of layers in the base model: ", len(base_model.layers))
    #print(base_model.layers[0].output_shape)
    x = base_model.output
    #x = tf.keras.layers.GlobalMaxPooling2D()(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(1024, activation = 'relu')(x)
    x = tf.keras.layers.Dense(512, activation = 'relu')(x)
    x = tf.keras.layers.Dense(64, activation = 'relu')(x)
    if num_class == 2:
        out = tf.keras.layers.Dense(1, activation = 'sigmoid')(x)
    if num_class > 2:
        out = tf.keras.layers.Dense(num_class, activation = "softmax")(x)
    model = tf.keras.models.Model(inputs = base_model.input, outputs = out)
    
    print('\n--------------Done!--------------')
    return model
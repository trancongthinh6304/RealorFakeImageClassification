import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
import time

def split_csv(df, val_split, seed):
    x_train, x_val, y_train, y_val = train_test_split(df.drop(columns = 'label',axis=1),
                                                      df['label'],
                                                      test_size = val_split,
                                                      shuffle = True,
                                                      random_state = seed)
    df_train_cut = pd.concat([x_train, y_train], axis = 1)
    df_val_cut = pd.concat([x_val, y_val], axis = 1)
    print(x_train.shape, x_val.shape)
    return df_train_cut, df_val_cut

def prep_fn(img):
    img = img.astype(np.float32) / 255.0
    img = (img - 0.5) * 2
    return img

def data_generator(df_train_cut, df_val_cut, data_path, img_size, batch_size, seed):
        start_time = time.time()

        training_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                                preprocessing_function = prep_fn,
                                horizontal_flip = True,
                                vertical_flip = True,
                                brightness_range = [0.8,1.5],
                                fill_mode = 'nearest')
        train_generator = training_datagen.flow_from_dataframe(
                                dataframe = df_train_cut,
                                directory = data_path,
                                x_col = "name",
                                y_col = "label",
                                target_size = (img_size, img_size),
                                batch_size = batch_size,
                                class_mode = 'binary',
                                shuffle = True,
                                seed = seed)

        validation_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                                preprocessing_function = prep_fn)
        val_generator = validation_datagen.flow_from_dataframe(
                                dataframe = df_val_cut,
                                directory = data_path,
                                x_col = "name",
                                y_col = "label",
                                target_size = (img_size, img_size),
                                batch_size = batch_size,
                                class_mode = 'binary',
                                shuffle = True,
                                seed = seed)

        print(f'----{time.time()-start_time} seconds----')
        return train_generator, val_generator
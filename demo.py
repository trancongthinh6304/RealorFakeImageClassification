import gradio as gr
import numpy as np
import cv2
from data_processing import *

def predict(img_path, model1, model2, clipping_ratio, ensemble_ratio, img_size):
  X = []
  X.append(cv2.resize(cv2.imread(img_path), dsize = (img_size, img_size)))
  X = np.array(X)
  X = prep_fn(X)
  pred1 = model1.predict(X)
  pred2 = model2.predict(X)
  clipped_pred1 = np.clip(pred1, clipping_ratio[0], clipping_ratio[1])
  clipped_pred2 = np.clip(pred2, clipping_ratio[0], clipping_ratio[1])
  ensemble_pred = ensemble_ratio*clipped_pred1 + (1-ensemble_ratio)*clipped_pred2
  print(ensemble_pred)

def gradio():
    im = gr.inputs.Image(tool = None, image_mode = 'RGB', type = 'file')
    iface = gr.Interface(
        fn = predict, 
        inputs = im, 
        outputs = "text",
        interpretation = "default"
    )
    
    iface.launch(debug = True)
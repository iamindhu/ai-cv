import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def gamma_function(channel, gamma):
    invGamma = 1/gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    channel = cv2.LUT(channel, table)
    return channel

def winter_filter(image): 
   image[:, :, 0] = gamma_function(image[:, :, 0], 1.25)
   image[:, :, 2] = gamma_function(image[:, :, 2], 0.75)
   hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   hsv[:, :, 1] = gamma_function(hsv[:, :, 1], 0.8)
   winter_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

   return winter_image

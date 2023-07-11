import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def gamma_function(channel, gamma):
    invGamma = 1/gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8") #creating lookup table
    channel = cv2.LUT(channel, table)
    return channel

def summer_filter(image): 
   # If image does not have 3 channels (BGR)
    if image.ndim != 3 or image.shape[2] != 3:
        try:
            # Convert to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    image[:, :, 0] = gamma_function(image[:, :, 0], 0.75) # down scaling blue channel
    image[:, :, 2] = gamma_function(image[:, :, 2], 1.25) # up scaling red channel
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = gamma_function(hsv[:, :, 1], 1.2) # up scaling saturation channel
    summer_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


    return summer_image

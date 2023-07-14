import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def hsv(image, l, u):
    # If the input image is grayscale
    if image.ndim != 3 or image.shape[2] != 3:
        try:
            # Convert to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([l,128,128]) # setting lower HSV value
    upper = np.array([u,255,255]) # setting upper HSV value
    mask = cv2.inRange(hsv, lower, upper) # generating mask
    return mask

def splash(image, l=15, u=30): 
    # Default values of Hue -  
    # lower (l=15) and upper (u=30)
    
    # If image does not have 2 channels (it is not grayscale)
    if image.ndim != 2:
        try:
            # Convert colored image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    else:
        gray = image.copy()
    res = np.zeros(image.shape, np.uint8) # creating blank mask for result
    res = res.reshape(image.shape[0], image.shape[1], -1)
    mask = hsv(image, l, u)
    inv_mask = cv2.bitwise_not(mask) # inverting mask
    res1 = cv2.bitwise_and(image, image, mask= mask) # region which has to be in color
    res2 = cv2.bitwise_and(gray, gray, mask= inv_mask) # region which has to be in grayscale
    for i in range(res.shape[-1]):
        res[:, :, i] = res2 # storing grayscale mask to all three slices
    splash_image = cv2.bitwise_or(res1, res) # joining grayscale and color region
    return splash_image

import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def brighten_image(image, brightness=1.25): 

   # If image does not have 3 channels (BGR)
   if image.ndim != 3 or image.shape[2] != 3:
       try:
           # Convert to BGR
           image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
       except Exception as e:
           # Return exception if image is neither grayscale nor colored
           return e
   
   hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert image to HSV color space
   hsv = np.array(hsv, dtype = np.float64)
   hsv[:,:,1] = hsv[:,:,1]*brightness # scale pixel values up for channel 1
   hsv[:,:,1][hsv[:,:,1]>255]  = 255
   hsv[:,:,2] = hsv[:,:,2]*brightness # scale pixel values up for channel 2
   hsv[:,:,2][hsv[:,:,2]>255]  = 255
   hsv = np.array(hsv, dtype = np.uint8)
   brightened_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # converting back to BGR used by OpenCV


   return brightened_image

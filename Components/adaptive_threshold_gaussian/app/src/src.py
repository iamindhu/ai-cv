import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def adaptive_threshold_gaussian(image, blocksize=199, const=5): 

      
   # cv2.cvtColor is applied over the
   # image input with applied parameters
   
   # If image does not have 2 channels (it is not grayscale)
   if image.ndim != 2:
       try:
           # Convert colored image to grayscale
           image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       except Exception as e:
           # Return exception if image is neither grayscale nor colored
           return e
      
   # applying different thresholding  on the input image
   
   adaptive_threshold_gaussian_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY, blocksize, const)
   
   return adaptive_threshold_gaussian_image

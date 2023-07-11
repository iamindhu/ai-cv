import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def adaptive_thresholding_mean(image): 
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

   # applying different thresholding the input image
   adaptive_thresholding_mean_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 199, 5)


   return adaptive_thresholding_mean_image

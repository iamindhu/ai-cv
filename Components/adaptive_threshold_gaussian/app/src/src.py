import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def adaptive_threshold_gaussian(image): 

      
   # cv2.cvtColor is applied over the
   # image input with applied parameters
   # to convert the image in grayscale 
   img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
   # applying different thresholding  on the input image
   
   adaptive_threshold_gaussian_image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY, 199, 5)
   
   return adaptive_threshold_gaussian_image

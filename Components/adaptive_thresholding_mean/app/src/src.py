import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def adaptive_thresholding_mean(image): 
   # cv2.cvtColor is applied over the
   # image input with applied parameters
   # to convert the image in grayscale 
   img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
   # applying different thresholding the input image
   adaptive_thresholding_mean_image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 199, 5)


   return adaptive_thresholding_mean_image

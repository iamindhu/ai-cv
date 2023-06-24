import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def truncated_thresholding(image): 
   ret, truncated_thresholded_image = cv2.threshold(image, 120, 255, cv2.THRESH_TRUNC)
   
   return truncated_thresholded_image

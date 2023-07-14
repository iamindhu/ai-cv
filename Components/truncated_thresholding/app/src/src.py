import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def truncated_thresholding(image, thresh=120): 
   ret, truncated_thresholded_image = cv2.threshold(image, thresh, 255, cv2.THRESH_TRUNC)
   
   return truncated_thresholded_image

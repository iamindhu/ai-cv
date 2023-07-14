import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def binary_thresholding(image, thresh=120): 
   ret, binary_thresholded_image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
   
   return binary_thresholded_image

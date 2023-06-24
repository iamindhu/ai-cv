import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def binary_thresholding(image): 
   ret, binary_thresholded_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
   
   return binary_thresholded_image

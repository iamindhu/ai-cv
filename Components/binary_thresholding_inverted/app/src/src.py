import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def binary_thresholding_inverted(image, thresh=120): 
   ret, binary_thresholding_inverted_image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY_INV)
   
   return binary_thresholding_inverted_image

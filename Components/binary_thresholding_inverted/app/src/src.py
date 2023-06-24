import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def binary_thresholding_inverted(image): 
   ret, binary_thresholding_inverted_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)
   
   return binary_thresholding_inverted_image

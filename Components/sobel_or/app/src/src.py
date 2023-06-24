import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def sobel_or(image): 

   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   x_sobel_image = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
   y_sobel_image = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
   sobel_or_image = cv2.bitwise_or(x_sobel_image, y_sobel_image)
   
   return sobel_or_image

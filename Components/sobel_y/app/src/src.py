import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def sobel_y(image): 

   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   y_sobel_image = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
   
   
   return y_sobel_image

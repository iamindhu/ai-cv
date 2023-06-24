import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def sobel_x(image): 

   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   x_sobel_image = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
   
   
   return x_sobel_image

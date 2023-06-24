import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def image_dialation(image): 
   kernel = np.ones((5, 5), np.uint8)
   dialated_image = cv2.dilate(image, kernel, iterations=1) 
   
   return dialated_image

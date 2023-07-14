import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def image_dialation(image, ksize=5, iters=1): 
   kernel = np.ones((ksize, ksize), np.uint8)
   dialated_image = cv2.dilate(image, kernel, iterations=iters) 
   
   return dialated_image

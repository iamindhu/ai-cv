import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def image_erosion(image, ksize=5, iters=1): 
   kernel = np.ones((ksize, ksize), np.uint8)
   dialated_image = cv2.erode(image, kernel, iterations=iters)
   
   return dialated_image

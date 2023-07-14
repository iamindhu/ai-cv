import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def opening(image, ksize=5): 
   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   kernel = np.ones((ksize, ksize), np.uint8)
   opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

   return opening_image

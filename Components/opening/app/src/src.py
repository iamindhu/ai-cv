import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def opening(image): 
   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   kernel = np.ones((5,5), np.uint8)
   opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

   return opening_image

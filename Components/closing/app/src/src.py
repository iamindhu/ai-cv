import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def closing(image): 

   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   kernel = np.ones((5,5), np.uint8)
   closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

   
   return closing_image

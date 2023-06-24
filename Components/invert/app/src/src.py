import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def invert_image(image): 
   
   inverted_image = cv2.bitwise_not(image)


   return inverted_image

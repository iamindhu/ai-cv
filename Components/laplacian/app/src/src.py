import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def laplacian(image): 

   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   laplacian_image = cv2.Laplacian(image, cv2.CV_64F)

   
   return laplacian_image

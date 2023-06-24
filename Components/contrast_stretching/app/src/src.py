import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def contrast_streching(image): 
   contrast_stretched_image = (cv2.normalize(image,None,105,135,cv2.NORM_MINMAX)-105)/(135-105) 
   
   return contrast_stretched_image

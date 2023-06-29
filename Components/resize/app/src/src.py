import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def resize(image, x=224, y=224):
    # Resize to new pixel size
    new_img = cv2.resize(image, (x,y))
    
    return new_img
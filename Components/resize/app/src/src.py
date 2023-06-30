import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def resize(image, x=224, y=None):
    
    if y is None:
        y=x
    # Resize to new pixel size
    new_img = cv2.resize(image, (x,y))
    
    return new_img
import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def flip_vertical(image):
    # Flip the image about the Y-axis
    flipped_image = cv2.flip(image, 0)
    
    return flipped_image

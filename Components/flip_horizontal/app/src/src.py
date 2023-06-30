import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def flip_horizontal(image):
    # Flip the image about the X-axis
    flipped_image = cv2.flip(image, 1)
    
    return flipped_image

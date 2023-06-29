import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def rescale(image, xscale=0.8, yscale=None):
    if yscale is None:
        yscale = xscale
    # Rescale image by input scaling factors
    new_img = cv2.resize(image, (0, 0), fx = xscale, fy = yscale)
    
    return new_img

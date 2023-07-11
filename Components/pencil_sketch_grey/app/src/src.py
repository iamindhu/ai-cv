import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def pencil_sketch_grey(image): 
    # If image does not have 3 channels (BGR)
    if image.ndim != 3 or image.shape[2] != 3:
        try:
            # Convert to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    
    pencil_sketch_grey_image, dst_color = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05) # inbuilt function to generate pencil sketch in both color and grayscale
    return pencil_sketch_grey_image

import cv2 
import numpy as np

def histogram_stretching(image):
    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the minimum and maximum pixel values
    min_val = np.min(grayscale)
    max_val = np.max(grayscale)

    # Perform histogram stretching
    stretched = cv2.normalize(grayscale, None, 0, 255, cv2.NORM_MINMAX)

    # Convert the image back to BGR color space
    stretched_image = cv2.cvtColor(stretched, cv2.COLOR_GRAY2BGR)

    return stretched_image
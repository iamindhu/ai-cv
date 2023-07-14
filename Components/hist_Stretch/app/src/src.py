import cv2 
import numpy as np

def histogram_stretching(image):
    
    # If image does not have 2 channels (it is not grayscale)
    if image.ndim != 2:
        try:
            # Convert colored image to grayscale
            grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    else:
        grayscale = image.copy()

    # Compute the minimum and maximum pixel values
    min_val = np.min(grayscale)
    max_val = np.max(grayscale)

    # Perform histogram stretching
    stretched = cv2.normalize(grayscale, None, 0, 255, cv2.NORM_MINMAX)

    # Convert the image back to BGR color space
    stretched_image = cv2.cvtColor(stretched, cv2.COLOR_GRAY2BGR)

    return stretched_image
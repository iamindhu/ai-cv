import cv2
import numpy as np

def extract_contours(image):
    
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

    # Apply thresholding to convert the image to binary
    _, threshold = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    # Draw contours on a blank canvas
    canvas = np.zeros_like(image)
    cv2.drawContours(canvas, contours, -1, (0, 255, 0), 1)

    return canvas

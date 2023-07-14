import cv2
import numpy as np

def extract_red_channel(image):

    # If image does not have 3 channels (BGR)
    if image.ndim != 3 or image.shape[2] != 3:
        try:
            # Convert to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    
    # Split the image into color channels
    channels = cv2.split(image)

    # Create an empty image with the same size as the input image
    red_channel = np.zeros_like(image)

    # Set the blue channel of the empty image to the blue channel of the input image
    red_channel[:, :, 2] = channels[2]

    return red_channel

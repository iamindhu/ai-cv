import cv2
import numpy as np

def gamma_correction(image, gamma=1.8):
    # Normalize the image intensity values to the range [0, 1]
    normalized_image = image / 255.0

    # Apply gamma correction
    corrected_image = np.power(normalized_image, gamma)

    # Rescale the image intensity values to the range [0, 255]
    corrected_image = np.uint8(corrected_image * 255)

    return corrected_image

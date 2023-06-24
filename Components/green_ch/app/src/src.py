import cv2
import numpy as np

def extract_green_channel(image):
    # Split the image into color channels
    channels = cv2.split(image)

    # Create an empty image with the same size as the input image
    green_channel = np.zeros_like(image)

    # Set the blue channel of the empty image to the blue channel of the input image
    green_channel[:, :, 1] = channels[1]

    return green_channel


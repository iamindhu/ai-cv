import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def features_hls(image):
    
    # If image does not have 3 channels (BGR)
    if image.ndim != 3 or image.shape[2] != 3:
        try:
            # Convert to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    
    # Convert to HLS
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    
    return hls

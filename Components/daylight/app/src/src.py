import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def daylight_filter(image, daylight=1.15): 
    # Default daylight intensity = 1.15

    # If image does not have 3 channels (BGR)
    if image.ndim != 3 or image.shape[2] != 3:
        try:
            # Convert to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    
    image_HLS = cv2.cvtColor(image,cv2.COLOR_BGR2HLS) # Conversion to HLS
    image_HLS = np.array(image_HLS, dtype = np.float64)

    image_HLS[:,:,1] = image_HLS[:,:,1]*daylight # scale pixel values up for channel 1(Lightness)
    image_HLS[:,:,1][image_HLS[:,:,1]>255]  = 255 # Sets all values above 255 to 255
    image_HLS = np.array(image_HLS, dtype = np.uint8)
    daylight_image = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2BGR) # Conversion to RGB


    return daylight_image

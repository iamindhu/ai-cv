import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def sepia(image): 

    # If image does not have 3 channels (BGR)
    if image.ndim != 3 or image.shape[2] != 3:
        try:
            # Convert to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    
    image = np.array(image, dtype=np.float64) # converting to float to prevent loss
    image = cv2.transform(image, np.matrix([[0.272, 0.534, 0.131],
                                        [0.349, 0.686, 0.168],
                                        [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
    image[np.where(image > 255)] = 255 # normalizing values greater than 255 to 255
    sepia_image = np.array(image, dtype=np.uint8) # converting back to int


    return sepia_image

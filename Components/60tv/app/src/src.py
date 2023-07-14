import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

def tv_60s(image, thresh=0.8): 
    # Default threshold = 0.8 i.e. noise will be added to 80% pixels

    # If image does not have 2 channels (it is not grayscale)
    if image.ndim != 2:
        try:
            # Convert colored image to grayscale
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e

    height, width = image.shape[:2]
    tv60 = image.copy()
     
    for i in range(height):
        for j in range(width):
            if np.random.rand() <= thresh:
                if np.random.randint(2) == 0:
                    tv60[i, j] = min(tv60[i, j] + np.random.randint(0, 64), 255) # adding random value between 0 to 64. Anything above 255 is set to 255.
                else:
                    tv60[i, j] = max(tv60[i, j] - np.random.randint(0, 64), 0) # subtracting random values between 0 to 64. Anything below 0 is set to 0.



    return tv60

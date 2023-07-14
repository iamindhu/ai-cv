import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def emboss(image): 
    height, width = image.shape[:2]
    y = np.ones((height, width), np.uint8) * 128
    embossed_image = np.zeros((height, width), np.uint8)
    # generating the kernels
    kernel1 = np.array([[0, -1, -1], # kernel for embossing bottom left side
                        [1, 0, -1],
                        [1, 1, 0]])
    kernel2 = np.array([[-1, -1, 0], # kernel for embossing bottom right side
                        [-1, 0, 1],
                        [0, 1, 1]])
    # you can generate kernels for embossing top as well
    # If image does not have 2 channels (it is not grayscale)
    if image.ndim != 2:
        try:
            # Convert colored image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e
    else:
        gray = image.copy()
    output1 = cv2.add(cv2.filter2D(gray, -1, kernel1), y) # emboss on bottom left side
    output2 = cv2.add(cv2.filter2D(gray, -1, kernel2), y) # emboss on bottom right side
    for i in range(height):
        for j in range(width):
            embossed_image[i, j] = max(output1[i, j], output2[i, j]) # combining both embosses to produce stronger emboss
    return embossed_image

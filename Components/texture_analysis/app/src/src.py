import cv2 
import numpy as np

def texture_analysis(image):
    
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

    # Apply LBP
    radius = 3
    num_points = 8 * radius
    lbp = cv2.ORB_create(radius=radius, nlevels=8, edgeThreshold=5, patchSize=8, WTA_K=2)

    # Compute the LBP descriptors
    keypoints = lbp.detect(gray, None)
    _, descriptors = lbp.compute(gray, keypoints)

    # Show the keypoints on the image
    image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(0, 0, 255), flags=0)

    return image_with_keypoints

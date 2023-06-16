import cv2 
import numpy as np

def texture_analysis(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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

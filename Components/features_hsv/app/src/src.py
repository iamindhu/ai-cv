import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def features_hsv(image):
    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    return hsv

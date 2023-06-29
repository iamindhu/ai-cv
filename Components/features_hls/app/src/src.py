import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def features_hls(image):
    # Convert to HLS
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    
    return hls

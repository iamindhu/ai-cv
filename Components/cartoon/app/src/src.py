import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def cartoonize(image): 
    edges1 = cv2.bitwise_not(cv2.Canny(image, 100, 200)) # for thin edges and inverting the mask obatined
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5) # applying median blur with kernel size of 5
    edges2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7) # thick edges
    dst = cv2.edgePreservingFilter(image, flags=2, sigma_s=64, sigma_r=0.25) # you can also use bilateral filter but that is slow
    # flag = 1 for RECURS_FILTER (Recursive Filtering) and 2 for  NORMCONV_FILTER (Normalized Convolution). NORMCONV_FILTER produces sharpening of the edges but is slower.
    # sigma_s controls the size of the neighborhood. Range 1 - 200
    # sigma_r controls the how dissimilar colors within the neighborhood will be averaged. A larger sigma_r results in large regions of constant color. Range 0 - 1
    cartoon_image = cv2.bitwise_and(dst, dst, mask=edges1) # adding thin edges to smoothened image
    return cartoon_image

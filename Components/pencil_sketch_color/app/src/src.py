import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def pencil_sketch_color(image): 
    pencil_sketch_grey_image, pencil_sketch_color_image = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05) # inbuilt function to generate pencil sketch in both color and grayscale
    return pencil_sketch_color_image

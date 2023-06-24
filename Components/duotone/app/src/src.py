import cv2 
import numpy as np 
# import matplotlib.pyplot as plt


def exponential_function(channel, exp):
    table = np.array([min((i**exp), 255) for i in np.arange(0, 256)]).astype("uint8") # creating table for exponent
    channel = cv2.LUT(channel, table)
    return channel

def tone(image, number):
    for i in range(3):
        if i == number:
            image[:, :, i] = exponential_function(image[:, :, i], 1.05) # applying exponential function on slice
        else:
            image[:, :, i] = 0 # setting values of all other slices to 0
    return image

def duotone(image): 
    duotone_image = tone(image, 1) # change second parameter to 0 for blue, 1 for green and 2 for red screen
    return duotone_image

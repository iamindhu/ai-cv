import cv2 

def histogram_equalization(image):
    # Convert image to grayscale if it's in color
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(image)
    
    return equalized_image
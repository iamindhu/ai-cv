import cv2 

def grayscale_image( image ): 

   # If image does not have 2 channels (it is not grayscale)
   if image.ndim != 2:
        try:
            # Convert colored image to grayscale
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            # Return exception if image is neither grayscale nor colored
            return e

   return image
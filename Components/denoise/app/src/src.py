import cv2 

def denoise_image(image):
    # Apply denoising

    if len(image.shape) > 2:
        denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    else:
        denoised_image = cv2.fastNlMeansDenoising(image, None, 10, 10, 7, 21)
    
    return denoised_image
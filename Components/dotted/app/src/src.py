import cv2 
import numpy as np 
from PIL import Image, ImageDraw
# import matplotlib.pyplot as plt


def dotted(image):
    
    img_size = (image.shape[1], image.shape[0])
    
    def cv_to_pix(img):
        new_img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_RGB2BGR).astype('uint8'))
        pix = new_img.load()
        return pix
    
    pixels = cv_to_pix(image)
    # Choose the pixelization length
    pixelization_length = 3
    
    # Define the pixelize and mask image
    pixelize_image = Image.new('RGBA', img_size)
    mask_image = Image.new('RGBA', img_size, 'black')
    
    x_units = int(img_size[0] / pixelization_length)
    y_units = int(img_size[1] / pixelization_length)
    
    draw = ImageDraw.Draw(pixelize_image)
    mask_draw = ImageDraw.Draw(mask_image)
    
    for i in range(0, x_units):
        for j in range(0, y_units):
            mask_draw.ellipse((i * pixelization_length, j * pixelization_length,
                      i * pixelization_length + pixelization_length - 1,
                      j * pixelization_length + pixelization_length - 1),
                     (255,255,255,0))
    
            total_red_intensity = total_green_intensity = total_blue_intensity = 0
            averaging_pixel_number = pixelization_length * pixelization_length
    
            for k in range(0, pixelization_length):
                for l in range(0, pixelization_length):
                    total_red_intensity += pixels[i * pixelization_length + k, j * pixelization_length + l][0]
                    total_green_intensity += pixels[i * pixelization_length + k, j * pixelization_length + l][1]
                    total_blue_intensity += pixels[i * pixelization_length + k, j * pixelization_length + l][2]
    
            average_red_intensity = int(total_red_intensity / averaging_pixel_number)
            average_green_intensity = int(total_green_intensity / averaging_pixel_number)
            average_blue_intensity = int(total_blue_intensity / averaging_pixel_number)
    
            draw.rectangle((i * pixelization_length, j * pixelization_length,
                            i * pixelization_length + pixelization_length - 1,
                            j * pixelization_length + pixelization_length - 1),
                            (average_red_intensity, average_green_intensity, average_blue_intensity))
    pixelize_image.paste(mask_image, mask=mask_image)
    #pixelize_image.save("result_new.png")
    dotted_rgb = cv2.cvtColor(np.asarray(pixelize_image),cv2.COLOR_RGB2BGR)
    return dotted_rgb

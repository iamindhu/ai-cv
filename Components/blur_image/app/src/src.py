import cv2 

def blurring_image(image, ksize=11): 
   # Default kernel size = 11

   filtered_image = cv2.medianBlur(image, ksize)
   # images = [image , edges_detected]
   # location = [121, 122] 
   # for loc, edge_image in zip(location, images): 
   #    plt.subplot(loc) 
   #    plt.imshow(edge_image, cmap='gray')
   return filtered_image
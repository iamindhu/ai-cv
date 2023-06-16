import cv2
import numpy as np

def hough_line_transform(image, threshold=100, min_line_length=50, max_line_gap=10):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Perform Hough transform for line detection
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold, minLineLength=min_line_length, maxLineGap=max_line_gap)

    # Draw the detected lines on a blank image
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Overlay the detected lines on the original image
    output_image = cv2.addWeighted(image, 0.8, line_image, 1, 0)

    return output_image
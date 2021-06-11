# Importing dependencies.
import cv2
import numpy as np
import util.basic as util
import matplotlib.pyplot as plt

# Resources
IMG_URL = "images/car.jpeg"
VIDEO_URL = "images/extras.mp4"
CAM_DEFAULT = 0

# Colors
TOMATO = (54, 65, 241)

if __name__ == "__main__":
    img = cv2.imread(IMG_URL)
    img = util.rescale_frame(img, scale=1)
    DIMENSIONS = img.shape
    DIMENSIONS_MONO = img.shape[:2]

    # Averaging
    avg_blurred = cv2.blur(img, (7, 7))
    avg_blurred = util.label(avg_blurred, "Average Blurring")

    # Gaussian Blur
    gaussian_blurred = cv2.GaussianBlur(img, (7, 7), 0)
    gaussian_blurred = util.label(gaussian_blurred, "Gaussian Blurring")

    # Median Blur
    median_blurred = cv2.medianBlur(img, 5)
    median_blurred = util.label(median_blurred, "Median Blurring")

    # Bilateral Blur | Retains Edge | Time Complexity >>
    bilateral_blurred = cv2.bilateralFilter(img, 20, 35, 35)
    bilateral_blurred = util.label(bilateral_blurred, "Bilateral Blurring")

    # Output Grid
    filler = util.clean_slate(DIMENSIONS, TOMATO)

    use_this = cv2.cvtColor(avg_blurred.copy(), cv2.COLOR_BGR2GRAY)

    # Thresholding
    ret, thresh_img = cv2.threshold(use_this, 125, 255, cv2.THRESH_BINARY)
    thresh_img = util.label(thresh_img, "Thresholding")

    # Canny Edge Detection
    canny_img = cv2.Canny(use_this, 125, 175, cv2.BORDER_DEFAULT)
    canny_img = util.label(canny_img, "Canny Edges")

    img_out = util.stack_images(
        0.4, ([bilateral_blurred, avg_blurred, thresh_img], [gaussian_blurred, median_blurred, canny_img]))
    cv2.imshow("output_grid", img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2
import numpy as np
import util.basic as util
import matplotlib.pyplot as plt

# Resources
IMG_URL = "images/digits.png"
VIDEO_URL = "images/dibyasom.mp4"
CAM_DEFAULT = 0

# Colors
TOMATO = (54, 65, 241)
SEMOLINA = (153, 184, 206)
PANTONE = (202, 220, 78)
MIDNIGHT_BLUE = (70, 47, 6)
BEIGE = (220, 240, 248)

if __name__ == "__main__":
    # stream = cv2.VideoCapture(VIDEO_URL)
    # _, img = stream.read()

    img = cv2.imread(IMG_URL)
    # img = util.rescale_frame(img, scale=1)
    DIMENSIONS = img.shape
    DIMENSIONS_MONO = img.shape[:2]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canvas = util.canvas_mono(img_gray.shape)

    # Simple Thresholding
    threshold, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    threshold, thresh_inverse = cv2.threshold(
        img_gray, 150, 255, cv2.THRESH_BINARY_INV)
    contours_simple, _ = cv2.findContours(
        thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    canvas_simple = cv2.drawContours(canvas.copy(), contours=contours_simple,
                                     contourIdx=-1, color=255, thickness=2)
    canvas_simple = util.label(canvas_simple, "Simple")

    # Adaptive Thresholding | CV will find the optimum thresholding value.
    adaptive_thresh = cv2.adaptiveThreshold(
        img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
    adaptive_thresh_inverse = cv2.adaptiveThreshold(
        img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
    contours_adaptive, _ = cv2.findContours(
        adaptive_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    canvas_adaptive = cv2.drawContours(canvas.copy(), contours_adaptive,
                                       contourIdx=-1, color=255, thickness=2)
    canvas_adaptive = util.label(canvas_adaptive, "Adaptive")

    # cv2.imshow("Canny Simple", contours_simple)
    # Output Grid
    img_out = util.stack_images(
        0.75, ([img, img_gray, canvas], [thresh, thresh_inverse, canvas_simple], [adaptive_thresh, adaptive_thresh_inverse, canvas_adaptive]))

    # img_out = util.label(img_out, "Thresholding!")

    cv2.imshow(__name__, img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

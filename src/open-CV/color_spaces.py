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
    img = util.rescale_frame(img, scale=0.3)

    DIMENSIONS = img.shape[:]

    # To grayscale
    img_mono = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Grayscale to BGR
    img_bgrED_gray = cv2.cvtColor(img_mono, cv2.COLOR_GRAY2BGR)

    # To HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # To LAB
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Output Grid
    filler = util.clean_slate(DIMENSIONS, TOMATO)

    img_out = util.stack_images(
        1, ([img, img_mono], [img_hsv, img_lab], [img_rgb, img_bgrED_gray]))
    cv2.imshow("output_grid", img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # plt.imshow(img_out)
    # plt.show()

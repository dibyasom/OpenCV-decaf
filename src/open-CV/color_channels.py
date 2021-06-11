# Importing dependencies.
import cv2
import numpy as np
import util.basic as util
import matplotlib.pyplot as plt

# Resources
IMG_URL = "images/rainbow.png"
VIDEO_URL = "images/extras.mp4"
CAM_DEFAULT = 0

# Colors
TOMATO = (54, 65, 241)

if __name__ == "__main__":
    img = cv2.imread(IMG_URL)
    img = util.rescale_frame(img, scale=1)
    DIMENSIONS = img.shape
    DIMENSIONS_MONO = img.shape[:2]

    b, g, r = cv2.split(img)
    blank = util.canvas_mono(DIMENSIONS_MONO)

    blue = cv2.merge([b, blank, blank])
    green = cv2.merge([blank, g, blank])
    red = cv2.merge([blank, blank, r])

    print(f"blank: {blank.shape}\nblue: {blue.shape}\n")
    # Merging color channels
    img_merged = cv2.merge([b, g, r])
    # Output Grid
    filler = util.clean_slate(DIMENSIONS, TOMATO)

    img_out = util.stack_images(
        1, ([img, b, g, r], [img_merged, blue, green, red]))
    cv2.imshow("output_grid", img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

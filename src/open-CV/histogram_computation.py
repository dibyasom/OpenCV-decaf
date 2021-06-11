# Importing dependencies.
import cv2
import numpy as np
import util.basic as util
import matplotlib.pyplot as plt

# Resources
IMG_URL = "images/dots.png"
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
    img = util.rescale_frame(img, scale=1)
    DIMENSIONS = img.shape
    DIMENSIONS_MONO = img.shape[:2]

    # Mask
    canvas = util.canvas_mono(img.shape[:2])
    mask = cv2.circle(
        canvas.copy(), (canvas.shape[1]//2, canvas.shape[0]//2), 100, 255, -1)
    img_mono = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    masked = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("Image", img_mono)
    cv2.imshow(IMG_URL, masked)
    cv2.waitKey(0)

    # Grayscale Histogram
    # gray_hist = cv2.calcHist([img_mono], [0], mask, [256], [0, 256])

    # Color Histogram
    plt.figure()
    plt.title("RGB Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    channels = ('b', 'g', 'r')
    for i, channel in enumerate(channels):
        hist = cv2.calcHist([img], [i], mask, [256], [0, 256])
        plt.plot(hist, color=channel)
        plt.xlim([0, 256])

    plt.show()

    cv2.destroyAllWindows()

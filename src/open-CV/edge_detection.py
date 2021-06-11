import cv2
import numpy as np
import util.basic as util
import matplotlib.pyplot as plt

# Resources
# IMG_URL = "images/digits.png"
IMG_URL = "images/car.jpeg"
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

    # Laplacian
    img_lap = cv2.Laplacian(img_gray, cv2.CV_64F)
    img_lap = np.uint8(np.absolute(img_lap))

    # Sobel
    img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0)
    img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1)

    # Output Grid
    filler = util.clean_slate(DIMENSIONS, TOMATO)

    img_out = util.stack_images(
        0.4, ([img, img_lap], [img_sobel_x, img_sobel_y]))
    cv2.imshow("output_grid", img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

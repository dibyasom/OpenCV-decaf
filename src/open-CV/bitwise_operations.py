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
SEMOLINA = (153, 184, 206)
PANTONE = (202, 220, 78)
MIDNIGHT_BLUE = (70, 47, 6)
BEIGE = (220, 240, 248)

if __name__ == "__main__":
    img = cv2.imread(IMG_URL)
    img = util.rescale_frame(img, scale=1)
    DIMENSIONS = img.shape
    DIMENSIONS_MONO = img.shape[:2]

    # Output Grid
    filler = util.clean_slate(DIMENSIONS, MIDNIGHT_BLUE)
    filler = util.label(filler, "Filler")

    FILLER_CENTER = (filler.shape[1]//2, filler.shape[0]//2)
    # Canvas
    blank = util.canvas_mono(filler.shape[:2])

    # Draw rectangle.
    rect = util.rect_center(blank, PANTONE, -1)

    # Draw Circle
    circle = cv2.circle(blank.copy(), FILLER_CENTER,
                        FILLER_CENTER[0]//2, TOMATO, -1)

    # Bitwise AND --> Intersecting Regions
    bitwise_and = cv2.bitwise_and(rect, circle)

    # Bitwise OR --> Non intersecting + Intersecting region
    bitwise_or = cv2.bitwise_or(rect, circle)

    # Bitwise XOR --> Non intersecting region
    bitwise_xor = cv2.bitwise_xor(rect, circle)

    # Bitwise NOT --> Inverts the colors
    bitwise_not = cv2.bitwise_not(rect)

    img_out = util.stack_images(
        0.4, ([rect, circle, bitwise_not], [bitwise_and, bitwise_or, bitwise_xor]))
    img_out = util.label(img_out, "Bitwise Operations")

    cv2.imshow("output_grid", img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

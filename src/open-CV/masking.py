# Importing dependencies.
import cv2
import numpy as np
import util.basic as util
import matplotlib.pyplot as plt

# Resources
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
    stream = cv2.VideoCapture(VIDEO_URL)
    _, img = stream.read()
    # img = util.rescale_frame(img, scale=0.67)
    DIMENSIONS = img.shape
    DIMENSIONS_MONO = img.shape[:2]

    # Create a Blank
    canvas = util.canvas_mono(img.shape[:2])
    # canvas = util.label(canvas.copy(), "Canvas")
    # cv2.imshow("Canvas", canvas)

    # Name | Rainbow --> Creating Mask
    text = ["@Alpha", "Dibyasom"]
    mask, base_height = util.label(canvas.copy(), text[0], True)
    mask = util.translate(mask.copy(), 0, int(base_height*1))
    mask, base_height = util.label(mask.copy(), text[1], True)

    while True:
        success, img = stream.read()

        if success:
            # img = util.rescale_frame(img, scale=0.67)
            masked = cv2.bitwise_and(img, img, mask=mask)
            cv2.imshow("Masked", masked)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    stream.release()
    cv2.destroyAllWindows()

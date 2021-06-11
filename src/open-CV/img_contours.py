import cv2
import numpy as np
from numpy.lib.function_base import _ureduce
from util.basic import stack_images

VIDEO_URL = "images/extras.mp4"
# IMAGE_URL = "images/digits.png"
IMAGE_URL = "images/dots.png"
DEFAULT_CAM = 0

# Colors
TOMATO = (54, 65, 241)


def rescale_frame(frame, scale=0.5):
    # Live video, static video/img
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)


def translate(src, x, y):
    # Translate (Shift image along x and y axis)
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (src.shape[1], src.shape[0])
    return cv2.warpAffine(img, translation_matrix, dimensions)


def rotate(src, angle, pivot=None, scale=1.0):
    # Rotate around a specific point as pivot.
    (height, width) = src.shape[:2]
    if not pivot:
        pivot = (width//2, height//2)
    rotation_matrix = cv2.getRotationMatrix2D(pivot, angle, scale)
    dimensions = (width, height)
    return cv2.warpAffine(src, rotation_matrix, dimensions)


def clean_slate(dimensions):
    return np.zeros(shape=dimensions, dtype='uint8')


if __name__ == "__main__":
    img = cv2.imread(IMAGE_URL)
    img_mono = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_mono_blurred = cv2.blur(
        img_mono, (5, 5), borderType=cv2.BORDER_DEFAULT)

    # Get edges
    img_canny = cv2.Canny(img_mono_blurred, 125, 175)

    ret, thresh = cv2.threshold(img_mono_blurred, 125, 220, cv2.THRESH_BINARY)
    # Find contours
    contours, heirarchies = cv2.findContours(
        img_canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Detected Contours: {len(contours)}")

    # Blank Slate
    canvas_salmon = clean_slate(img.shape)
    canvas_salmon[:] = 70, 47, 6
    for ctr in contours:
        print(f"Contour Area = {cv2.contourArea(ctr)}")
        if 100 <= cv2.contourArea(ctr) <= 300:
            print("Etching it <3")
            cv2.drawContours(canvas_salmon, contours=ctr,
                             contourIdx=-1, color=TOMATO, thickness=3)
        else:
            print("Skipping :(")
    # contours, heirarchies = cv2.findContours(
    #     img_canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    img_out = stack_images(
        1.8, ([img, img_mono], [img_canny, canvas_salmon]))

    cv2.imshow(__name__, img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

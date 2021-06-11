import cv2
import numpy as np
from util.join import stack_images

VIDEO_URL = "images/extras.mp4"
IMAGE_URL = "images/car.jpeg"
DEFAULT_CAM = 0


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


if __name__ == "__main__":
    img = cv2.imread(IMAGE_URL)
    img_shifted = translate(img, 300, 300)
    img_rotated = rotate(img, 180)
    img_flip = cv2.flip(img, 0)  # Flip vertically
    img_flip = cv2.flip(img, 1)  # Flip horizontally
    img_flip = cv2.flip(img, -1)  # Flip vertical+horizontal
    # Output grid.
    img_out = stack_images(
        0.4, ([img, img_shifted], [img_rotated, img_flip]))
    cv2.imshow("Translate", img_out)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

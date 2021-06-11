import cv2
from numpy.core.shape_base import stack
from util.join import stack_images

VIDEO_URL = "images/extras.mp4"
IMAGE_URL = "images/digits.png"
DEFAULT_CAM = 0


def rescale_frame(frame, scale=0.5):
    # Live video, static video/img
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)


img = cv2.imread(IMAGE_URL)

# Blurred conversion
img_blurred = cv2.blur(img, (7, 7), borderType=cv2.BORDER_DEFAULT)

# Detect Edges
img_canny_blurred = cv2.Canny(img_blurred, 125, 175)

# Dilation | Dilating the structural elements (Canny Edges)
img_dialted = cv2.dilate(img_canny_blurred, (5, 5), iterations=5)

# Erosion
img_erorded = cv2.erode(img_dialted, (5, 5), iterations=5)

# # Resize
# img_scaled_up = rescale_frame(img, scale=2)

img_out = stack_images(
    1.0, ([img, img_blurred], [img_canny_blurred, img_dialted]))
cv2.imshow(IMAGE_URL, img_out)
# cv2.imshow("Scaled_UP", img_scaled_up)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import util.basic as util

IMG_URL = "images/venom.jpg"

img = cv2.imread(IMG_URL)
img_l, img_r = img[:, :1920], img[:, 1921:]

cv2.imshow(f"Dims: {img.shape}", img_l)
cv2.imshow(f"Dims: {img_l.shape}", img_r)

cv2.imwrite("left.jpg", img_l)
cv2.imwrite("right.jpg", img_r)
cv2.waitKey(0)

import cv2
import numpy as np
import util.basic as util
import matplotlib.pyplot as plt
from skimage import measure

# Resources
# IMG_URL = "images/digits.png"
IMG_URL = "images/qr-blur.png"
VIDEO_URL = "images/dibyasom.mp4"
CAM_DEFAULT = 0

# Colors
TOMATO = (54, 65, 241)
SEMOLINA = (153, 184, 206)
PANTONE = (202, 220, 78)
MIDNIGHT_BLUE = (70, 47, 6)
BEIGE = (220, 240, 248)


def create_mask(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)
    _, thresh_img = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
    thresh_img = cv2.erode(thresh_img, None, iterations=3)
    thresh_img = cv2.dilate(thresh_img, None, iterations=3)
    # perform a connected component analysis on the thresholded image,
    # then initialize a mask to store only the "large" components
    labels = measure.label(thresh_img, connectivity=2, background=0)
    mask = np.zeros(thresh_img.shape, dtype="uint8")
    # loop over the unique components
    for label in np.unique(labels):
        # if this is the background label, ignore it
        if label == 0:
            continue
        # otherwise, construct the label mask and count the
        # number of pixels
        labelMask = np.zeros(thresh_img.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)
        # if the number of pixels in the component is sufficiently
        # large, then add it to our mask of "large blobs"
        if numPixels > 300:
            mask = cv2.add(mask, labelMask)
    return mask


if __name__ == "__main__":
    # stream = cv2.VideoCapture(VIDEO_URL)
    # _, img = stream.read()

    img = cv2.imread(IMG_URL)
    # img = util.rescale_frame(img, scale=1)
    DIMENSIONS = img.shape
    DIMENSIONS_MONO = img.shape[:2]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_hist_eql = cv2.equalizeHist(img_gray)
    img_hist_eql = cv2.equalizeHist(img_hist_eql)
    img_glared_mask = create_mask(img)
    img_glared_zone = cv2.bitwise_and(img_gray, img_glared_mask)
    img_glared_zone_fix = cv2.equalizeHist(img_glared_zone)
    img_normalized = cv2.inpaint(img, img_glared_mask, 5, cv2.INPAINT_NS)

    img_xor = cv2.bitwise_xor(img_gray, img_glared_zone_fix)
    img_xor_basic = cv2.bitwise_xor(img_gray, img_glared_zone)
    img = util.label(img, "Glared Img")
    img_gray = util.label(img_gray, "Img grayscale")
    img_glared_mask = util.label(img_glared_mask, "Glared Zone")
    img_normalized = util.label(img_normalized, "Glare Zone Removed")

    # Output Grid
    filler = util.clean_slate(DIMENSIONS, TOMATO)

    img_out = util.stack_images(
        1, ([img, img_gray], [img_glared_mask, img_normalized], [img_xor_basic, img_xor]))

    # cv2.imshow("output_grid", img_out)
    cv2.imwrite("glare.png", img_out)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

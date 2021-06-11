from os.path import isfile, join, exists
from os import listdir, makedirs
import cv2
import numpy as np
from skimage import measure

INPUT_DIR_PATH = "images/raw"
FILE_EXT_ALLOWED = ['jpeg', 'jpg', 'png']
OUTPUT_IMG_PREFIX = "masked"
OUTPUT_DIR_PATH = "processedFrames"


def nothing(x):
    pass


def rescale_frame(frame):
    # Live video, static img
    scale = 255/frame.shape[0]
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)


def create_mask(img, low, high):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low, high)
    return cv2.bitwise_and(img, img, mask=mask)


def create_mask_iter(image, h_thresh, l_thresh):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)
    _, thresh_img = cv2.threshold(
        blurred, l_thresh, h_thresh, cv2.THRESH_BINARY_INV)
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
    return cv2.bitwise_and(image, image, mask=mask)


if __name__ == "__main__":
    imgInDir = [join(INPUT_DIR_PATH, file) for file in listdir(
        INPUT_DIR_PATH) if (isfile(join(INPUT_DIR_PATH, file)) and file.split('.')[1] in FILE_EXT_ALLOWED)]

    cv2.namedWindow("trackbar")
    cv2.createTrackbar("L-H", "trackbar", 0, 179, nothing)
    cv2.createTrackbar("L-S", "trackbar", 0, 255, nothing)
    cv2.createTrackbar("L-V", "trackbar", 0, 255, nothing)
    cv2.createTrackbar("U-H", "trackbar", 179, 179, nothing)
    cv2.createTrackbar("U-S", "trackbar", 255, 255, nothing)
    cv2.createTrackbar("U-V", "trackbar", 255, 255, nothing)
    cv2.createTrackbar("U-Thresh", "trackbar", 255, 255, nothing)
    cv2.createTrackbar("L-Thresh", "trackbar", 0, 255, nothing)

    frame = cv2.imread(imgInDir[0])
    frame = rescale_frame(frame)

    if imgInDir:
        print(f"Images scanned :\n{imgInDir}")

        while True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            l_h = cv2.getTrackbarPos("L-H", "trackbar")
            l_s = cv2.getTrackbarPos("L-S", "trackbar")
            l_v = cv2.getTrackbarPos("L-V", "trackbar")
            h_h = cv2.getTrackbarPos("U-H", "trackbar")
            h_s = cv2.getTrackbarPos("U-S", "trackbar")
            h_v = cv2.getTrackbarPos("U-V", "trackbar")

            h_t = cv2.getTrackbarPos("U-Thresh", "trackbar")
            l_t = cv2.getTrackbarPos("L-Thresh", "trackbar")

            low = np.array([l_h, l_s, l_v])
            high = np.array([h_h, h_s, h_v])

            masked_img_iter = create_mask_iter(frame, h_t, l_t)
            masked_img = create_mask(masked_img_iter.copy(), low, high)
            cv2.imshow("Mask Thresh", masked_img_iter)
            cv2.imshow("Mask", masked_img)

            key = cv2.waitKey(1)

            # 'e' pressed
            if key == ord('e'):
                # Applying same mask to all images in dir. <3
                print("Extracting Masks.")
                hsv_f, thresh_f = f"{OUTPUT_DIR_PATH}/HSV-Mask", f"{OUTPUT_DIR_PATH}/Thresholding"
                if not exists(OUTPUT_DIR_PATH):
                    makedirs(hsv_f)
                    makedirs(thresh_f)

                for count, imgLoc in enumerate(imgInDir):
                    frame = cv2.imread(imgLoc)
                    frame = rescale_frame(frame)  # 255*255*3

                    # Create HSV Mask
                    masked_img = create_mask(frame, low, high)
                    # Create Thresholded Mask
                    masked_img_iter = create_mask_iter(frame, h_t, l_t)

                    cv2.imwrite(
                        join(hsv_f, f"{OUTPUT_IMG_PREFIX}-{count}.png"), masked_img)
                    cv2.imwrite(
                        join(thresh_f, f"{OUTPUT_IMG_PREFIX}-{count}.png"), masked_img_iter)
                print(
                    f"Successfully extractd masks, written to {OUTPUT_DIR_PATH}\nCount: {len(imgInDir)}")
                break

            # 'esc' pressed
            if key == 27:
                break
    else:
        print(f"No image file found in given path. {INPUT_DIR_PATH}")

    cv2.destroyAllWindows()

# Optimise for efficient runtime
import cv2
IMG_URL = "images/4k.jpg"
VIDEO_URL = "images/extras.mp4"
DEFAULT_CAM = 0


def rescale_frame(frame, scale=0.5):
    # Live video, static video/img
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def change_res(width, height):
    # Live video
    global stream
    stream.set(3, width)
    stream.set(4, height)
    stream.set(10, 30)


# Rescale Video


if __name__ == "__main__":

    stream = cv2.VideoCapture(DEFAULT_CAM)
    change_res(480, 320)
    streamMsg = (f"Stream loaded, {stream.get(3)}px x {stream.get(4)}px ")
    print(streamMsg)

    while True:
        successful, frame = stream.read()
        if successful:
            # frame = rescale_frame(frame)
            cv2.imshow(VIDEO_URL, frame)

        if cv2.waitKey(20) & 0xFF == ord('s'):
            break

    stream.release()
    cv2.destroyAllWindows()

import cv2
import numpy as np
from numpy.testing._private.utils import clear_and_catch_warnings

DEFAULT_CAM = 0
DIMENSION = (320, 240)


def change_res(dim):
    # Live video
    global stream
    stream.set(3, dim[0])
    stream.set(4, dim[1])
    stream.set(10, 30)


def clean_slate(dimensions, color=(0, 0, 0)):
    slate = np.zeros(shape=dimensions, dtype='uint8')
    slate[:] = color
    return slate


def stitch(frame_1, frame_2):
    dim = [px for px in frame_1.shape]
    dim[1] *= 2
    canvas = clean_slate(tuple(dim))
    dim[1] //= 2
    try:
        canvas[0:dim[0], 0:dim[1]] = frame_1[:, :]
    except ValueError:
        pass

    try:
        canvas[0:dim[1], dim[1]:dim[1]*2] = frame_2[:, :]
    except ValueError:
        print(np.shape(frame_2),  np.shape(frame_2[0]), np.shape(frame_2[1]))
        channelled_canvas = clean_slate(tuple(dim))
        for x in range(len(frame_2)):
            for y in range(len(frame_2[0])):
                channelled_canvas[x][y] = (
                    frame_2[x][y], frame_2[x][y], frame_2[x][y])
        canvas[0:dim[1], dim[1]:dim[1]*2] = channelled_canvas[:, :]
    return canvas


def rect_center(src):
    origin = (src.shape[1]//4, src.shape[0]//4)
    corner = (src.shape[1]*3//4, src.shape[0]*3//4)
    color = (162, 179, 65)
    cv2.rectangle(src, origin, corner, color, 2)


if __name__ == "__main__":
    stream = cv2.VideoCapture(DEFAULT_CAM)
    change_res(DIMENSION)
    streamMsg = (f"Stream loaded, {stream.get(3)}px x {stream.get(4)}px ")
    print(streamMsg)

    _, frame_dummy = stream.read()
    canvas_salmon = clean_slate(frame_dummy.shape)
    canvas_salmon[:] = 95, 125, 255

    # Circle
    cv2.circle(canvas_salmon,
               (canvas_salmon.shape[1]//2, canvas_salmon.shape[0]//2), 90, (62, 179, 165), -1)
    rect_center(src=canvas_salmon)
    # Line
    cv2.line(canvas_salmon, (0, 0),
             (canvas_salmon.shape[1], canvas_salmon.shape[0]), (162, 176, 65), 7)

    # Text
    cv2.putText(canvas_salmon, "Dev</>", (0, 50),
                cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 125, 255), 2)

    while True:
        successful, frame = stream.read()
        if successful:
            # frame = rescale_frame(frame)
            frame = stitch(frame, canvas_salmon)
            cv2.imshow("Matrix", frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    stream.release()
    cv2.destroyAllWindows()

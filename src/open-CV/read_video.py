import cv2

VIDEO_URL = "https://cdn.videvo.net/videvo_files/video/free/2020-12/small_watermarked/201202_01_Oxford%20Shoppers_4k_008_preview.webm"

# Stream is an instance of vidcap class
stream = cv2.VideoCapture(VIDEO_URL)

while True:
    successful, frame = stream.read()
    if successful:
        cv2.imshow(VIDEO_URL, frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

stream.release()
cv2.destroyAllWindows()

from imutils.video import VideoStream
import time
import cv2

videoStream = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    frame = videoStream.read()
    cv2.imshow("asd", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoStream.stop()

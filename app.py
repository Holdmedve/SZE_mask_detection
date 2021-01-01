from imutils.video import VideoStream
import time
import cv2

videoStream = VideoStream(src=0).start()
time.sleep(2.0)  # let the camera sensor warm up

while True:
    frame = videoStream.read()
    cv2.imshow("asd", frame)

    # 0xFF masks the returned 32 bit by waitKey()
    # we care about ASCII inputs
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoStream.stop()

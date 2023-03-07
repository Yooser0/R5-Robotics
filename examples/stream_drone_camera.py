import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
while True:
    frame_read = tello.get_frame_read().frame
    cv2.imshow('frame',frame_read)
    cv2.waitKey(1)

cv2.imwrite("picture2.png", frame_read)

#end connection
tello.streamoff()
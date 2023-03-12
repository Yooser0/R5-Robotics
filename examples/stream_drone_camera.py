import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
while True:
    frame_read = tello.get_frame_read().frame
    cv2.imshow('frame',frame_read)
    if cv2.waitKey(1) == ord('q'):#Press q to quit loop
            cv2.imwrite("./src/picture.png", frame_read)
            break


#end connection
tello.streamoff()
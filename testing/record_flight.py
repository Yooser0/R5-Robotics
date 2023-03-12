from djitellopy import Tello
import cv2
import numpy as np
import pandas as pd


from positioning import change_position

import threading
import time
import os

"""Gathers images and positions for the drone to create a map of environment
Currently for testing by manually moving drone around
TODO: Implement automatic movement of drone
""" 


tello = Tello()
tello.connect()
tello.streamon()

positions = pd.DataFrame(columns=['x', 'y', 'z', 'barometric'])
coords = [0.0, 0.0, 0.0]
thread = threading.Thread(target=change_position, args=(coords, tello)).start()

log_path = os.path.join(os.path.dirname(__file__), 'flight_logs')

i=0
#Start the video stream, capture images, positions, and save them
while True:
    #Read the current frame
    frame = tello.get_frame_read().frame
    #Save current position to csv
    positions = positions.append({'x': coords[0], 'y': coords[1], 'z': coords[2], 'barometric': tello.get_barometer()}, ignore_index=True)
    
    #Show and save the frame
    cv2.imshow('frame', frame)
    try:
        cv2.imwrite(f'{log_path}/frame_{i}.png', frame)
    except:
        print(f'Error saving image at {log_path}/frame_{i}.png')
        break
    time.sleep(.5)
    
    i+=1
    #Press q to quit loop
    if cv2.waitKey(1) == ord('q'):
        break

tello.streamoff()
#end processing thead
# thread.join()
cv2.destroyAllWindows()

#Count number of folders in flight_logs
num_flights = len([name for name in os.listdir(log_path) if os.path.isdir(os.path.join(log_path, name))])
#Create a new folder for the current flight
new_log_path = f'{log_path}/flight_{num_flights+1}'
os.mkdir(new_log_path)
#Save the positions to the new folder
positions.to_csv(f'{new_log_path}/positions.csv')

images=[img for img in os.listdir(log_path) if img.endswith('.png')]
print(images)
frame = cv2.imread(os.path.join(log_path, images[0]))
h,w,l = frame.shape

video = cv2.VideoWriter(f'{new_log_path}/flight_vid.avi', 0, 1, (w,h))
for image in images:
    video.write(cv2.imread(os.path.join(log_path, image)))
video.release()
#delete images
for image in images:
    print(f'Deleting {image}...')
    os.remove(os.path.join(log_path, image))



import cv2
import os
import time

def capture_images(num_images, folder_name = 'calibration_images', delay = 2):
    #check if folder exists
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    #capture images
    for i in range(num_images):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite(folder_name + '/image' + str(i) + '.jpg', frame)
        print('Captured image ' + str(i) + '.jpg ...')
        #delay 5 seconds between captures
        time.sleep(delay)
        cv2.imshow('frame', frame)
        cv2.waitKey(0)

def capture_images_drone(num_images=20, folder_name = 'calibration_images', delay = 2):
    """Used to collect images for calibration from the drone. Move the checkerboard calibration image
    around in the drone's field of view to get a good spread of images. Try to get a variery of orientations and
    positions.
    
    Reccomended a minimum of 20 images.
    Different for every camera, CANNOT assume to be same between drones
    Ensure checkerboard is flat (i.e not folded or warped).
    Try not to have the checkerboard too close to the edge of the frame, want entire thing in view for all pics.

    Args:
        num_images (int, optional): Number of images to capture. Defaults to 20.
        folder_name (str, optional): Folder to store images in. Defaults to 'calibration_images'.
        delay (int, optional): Number of seconds between captures. Defaults to 2.
    """
    
    #check if folder exists
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    #capture images
    from djitellopy import Tello

    tello = Tello()
    tello.connect()

    tello.streamon()
    for i in range(num_images):
        frame_read = tello.get_frame_read().frame
        cv2.imwrite(folder_name + '/tello_image' + str(i) + '.jpg', frame_read)
        print('Captured image ' + str(i) + '.jpg ...')
        time.sleep(delay)
    tello.streamoff()
    
time.sleep(5)
print('GOING FOR IT!!---------\n\n\n')
# capture_images_drone(5,'box_images/set_1', 2)
capture_images(5,'box_images/set_3', 2)

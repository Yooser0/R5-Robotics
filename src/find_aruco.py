import cv2
import numpy as np
import os
import yaml

#NOTE: OPENCV VERSION MUST BE AT LEAST 4.7.0

#Generate Aruco marker
SIDE_LEN_PX = 1000
SIDE_LEN_MM = 205.0

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
aruco_img = aruco_dict.generateImageMarker(1, SIDE_LEN_PX)#id 1 out of 6X6_50 dictionary

#Load camera parameters
#access camera parameters yaml one directory up, one over, and one down from current file
    #Should be ..\calibration\camera_params.yaml


# cam_mat_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'calibration','drone_calibration_matrix.yaml')
#NOTE: THIS IS FOR THE BAXTER CAMERA, FOR TESTING PURPOSES. CHANGE TO DRONE CAMERA WHEN USING DRONE CAMERA
cam_mat_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'calibration','baxter_webcam_calibration_matrix.yaml')
with open(cam_mat_path, 'r') as f:
    full = yaml.load(f, Loader=yaml.FullLoader)
    camera_matrix = np.array(full['camera_matrix'])
    t_vects = np.array(full['tvecs'])
    r_vects = np.array(full['rvecs'])
    dist_coeffs = np.array(full['dist_coeff'])

def undistort_img(img, camera_matrix, dist_coeff):
    """Undistort an image using the calibration matrix and distortion coefficients

    Args:
        img (np.array): Image to undistort
        matrx (np.array): Calibration matrix
        dist (np.array): Distortion coefficients

    Returns:
        np.array: Undistorted image
    """
    unwarped = cv2.undistort(img, camera_matrix, dist_coeff, None, camera_matrix)
    return unwarped

def generate_arucos(num_markers, dict = aruco_dict, side_len_px = SIDE_LEN_PX):
    """Generates aruco markers and saves them to a folder. Only needs to be run once, and then the images can be used for the rest of the time.

    Args:
        num_markers (int): Number of markers to generate
        dict (cv2 Dictionary, optional): cv2 object containing aruco information (tells opencv what to look for, what the id is, etc). Defaults to aruco_dict.
        side_len_px (int, optional): Length of side of marker in pixels. Defaults to SIDE_LEN_PX.

    Returns:
        None: Saves images to folder
    """
    #Create empty image to draw on
    aruco_img = np.zeros((side_len_px, side_len_px, 3), np.uint8)
    #Create folder to save images to (if it doesn't already exist)

    imagePath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'reference_images','aruco_markers')
    if not os.path.exists(os.path.join(imagePath, 'aruco_1.png')):
        for i in range(1, 12):   
            aruco_img = dict.generateImageMarker(i, side_len_px, aruco_img)
            cv2.imwrite(os.path.join(imagePath, f'aruco_{i}.png'), aruco_img)
            
def find_aruco(img, dict = aruco_dict, detector_params = cv2.aruco.DetectorParameters()):
    """Looks for aruco markers within image. Only in camera coordinate frame, NOT IN REAL WORLD COORDINATE FRAME

    Args:
        img (_type_): image from camera (or file)
        dict (_type_, optional): cv2 object containing aruco information (tells opencv what to look for, what the id is, etc). Defaults to aruco_dict.
        detector_params (_type_, optional): Some parameters for the detector class. Shouldn't need to modify ever. Defaults to cv2.aruco.DetectorParameters().

    Returns:
        Bool: True if markers are found, False if not
        np.array: Corners in image of aruco markers, should be 4 corners per marker. Returns None if no markers are found
    """
    #Convert to grayscale (required for detector)
    gray = img.copy()
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    
    #Cretae detector object
    detector = cv2.aruco.ArucoDetector(dict, detector_params)
    #detect markers in img
    corners, ids, rejectedImgPoints = detector.detectMarkers(gray)
    if(ids is not None):
        #If there is a marker in frame, log corner locations, and draw circles on them in original color image
        print(f'Found {len(ids)} markers')
        objPts = []
        for corner in corners[0]:
            for c in corner:
                pt = np.array([c[0], c[1]]).astype(int)
                objPts.append(pt)
                cv2.circle(img, tuple(pt), 5, (0,0,255), -1)
        #Return array of corner coordinates in camera reference frame
        return True, np.array(objPts)
    else:
        #If no markers are found, return None
        return False, None

def calc_pose(img, corners, camera_matrix, dist_coeffs = np.zeros((4,1))):
    """Calculates 6DOF pose of aruco markers in image in real world coordinate frame.
    Uses the solvePnP() function from OpenCV to determine the pose of the markers in the image based on intrinsic camera parameters and the marker's size.

    Args:
        img (_type_): cv2 image from camera (or file)
        corners (_type_): list of corners of aruco markers in image, already found
        camera_matrix (_type_): Intrinsic camera parameters expressed as matrix. Should be 3x3, generated from calibration script
        dist_coeffs (_type_): Distortion coefficients. Should be zero if camera is not majorly distorted. Defaults to np.zeros((4,1)).

    Returns:
        Bool: True if pose is found, False if not
        np.array: rotation vectors expressed as euler angles
        np.array: translation vectors relative to camera in x,y,z coordinates (cm)
    """
    #Create array of 3D points for each corner of the aruco marker (in mm) to represent original pts in 3D space
    obj_pts_3d = np.array([
        [0, 0, 0],#top left of aruco marker
        [SIDE_LEN_MM, 0, 0],#top right of aruco marker
        [SIDE_LEN_MM, SIDE_LEN_MM, 0],#bottom right of aruco marker
        [0, SIDE_LEN_MM, 0]#bottom left of aruco marker
    ]).astype(np.float64)#NOTE: Need to convert to float64 for solvePnP() to work
    
    #Create array of 2D points for each corner of the aruco marker (in pixels) to represent image pts in 2D space
    img_pts_2d = np.array(corners).astype(np.float64)#NOTE: Need to convert to float64 for solvePnP() to work

    # success, rotation_vector, translation_vector = cv2.solvePnP(obj_pts_3d, img_pts_2d, camera_matrix, dist_coeffs)
    success, rotation_vector, translation_vector, inliers = cv2.solvePnPRansac(obj_pts_3d, img_pts_2d, camera_matrix, dist_coeffs)
    rotation_vector = np.degrees(rotation_vector)

    if success:
        print(f'Found pose of marker: \n{translation_vector}\n{rotation_vector}')
        cv2.putText(img, f'{translation_vector/10}cm', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 2)

        #NOTE: Consder using solvePnPRansac() instead of solvePnP() to improve accuracy?
        #NOTE: Consider using sovlePnPRefineLM() to use non-linear Levenberg-Marquardt minimization scheme to refine pose estimate (Bunch of sci-fi words, not sure why it's better)

        return True, rotation_vector, translation_vector
    else:
        print('Failed to find pose')
        return False, None, None
        
#Testing with computer webcam
cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    #Cruical to undistort image before finding aruco markers
    img = undistort_img(img, camera_matrix, dist_coeffs)
    if ret:
        #Find aruco markers in image (returns corners of markers in image)
        corner_success, corners = find_aruco(img, aruco_dict)
        if corner_success:
            #Calculate pose of aruco markers in image (returns rotation and translation vectors)
            pose_success, rotation_vector, translation_vector = calc_pose(img, corners, camera_matrix, dist_coeffs)
            if pose_success:
                print(f'Found pose of markers: \n{translation_vector}\n{rotation_vector}')
        cv2.imshow('img', img)
        
        
        if cv2.waitKey(1) == ord('q'):#Press q to quit loop
            break

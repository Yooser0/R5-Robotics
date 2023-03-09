import cv2
import numpy as np
import os
import yaml

#NOTE: OPENCV VERSION MUST BE AT LEAST 4.7.0
#NOTE: Find 3d location from solvePnp() func at https://docs.opencv.org/4.7.0/d9/d0c/group__calib3d.html#ga549c2075fac14829ff4a58bc931c033d


#Generate Aruco marker
imagePath = 'Aruco_Markers'
SIDE_LEN_PX = 1000
SIDE_LEN_MM = 205.0

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
aruco_img = aruco_dict.generateImageMarker(1, SIDE_LEN_PX)

#Load camera parameters
#access camera parameters yaml file up, over, and down one directory
    #Should be ..\calibration\camera_params.yaml
cam_mat_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'calibration','calibration_matrix.yaml')
with open(cam_mat_path, 'r') as f:
    full = yaml.load(f, Loader=yaml.FullLoader)
    camera_matrix = np.array(full['camera_matrix'])
    t_vects = np.array(full['tvecs'])
    r_vects = np.array(full['rvecs'])
    
    

def generate_arucos(num_markers):
    aruco_img = np.zeros((SIDE_LEN_PX, SIDE_LEN_PX, 3), np.uint8)
    if not os.path.existt(os.path.join(imagePath, 'aruco_1.png')):
        for i in range(1, 12):   
            aruco_img = aruco_dict.generateImageMarker(i, SIDE_LEN_PX, aruco_img)
            cv2.imwrite(os.path.join(imagePath, f'aruco_{i}.png'), aruco_img)
def find_aruco(img, dict = aruco_dict, detector_params = cv2.aruco.DetectorParameters()):
    gray = img.copy()
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    
    detector = cv2.aruco.ArucoDetector(dict, detector_params)
    corners, ids, rejectedImgPoints = detector.detectMarkers(gray)
    if(ids is not None):
        print(ids)
        objPts = []
        for corner in corners[0]:
            for c in corner:
                pt = np.array([c[0], c[1]]).astype(int)
                objPts.append(pt)
                cv2.circle(img, tuple(pt), 5, (0,0,255), -1)
def calc_pose(img, corners, ids, camera_matrix, dist_coeffs):
    rvecs, tvecs, _objPoints = cv2.aruco.estimatePoseSingleMarkers(corners, SIDE_LEN_MM, camera_matrix, dist_coeffs)
    for i in range(len(ids)):
        cv2.aruco.drawAxis(img, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], 100)
        cv2.putText(img, str(ids[i][0]), tuple(corners[i][0][0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return rvecs, tvecs, _objPoints
        



# cam = cv2.VideoCapture(0)
# while True:
#     ret, img = cam.read()
#     if ret:
#         find_aruco(img, aruco_dict)
#         cv2.imshow('img', img)
#         if cv2.waitKey(1) == ord('q'):
#             break

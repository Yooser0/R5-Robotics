import cv2
import numpy as np
import yaml

#open the calibration matrix file
with open('calibration_matrix.yaml') as f:
    yaml_file = yaml.safe_load(f)
    camera_matrix = np.array(yaml_file['camera_matrix'])
    dist_coeff = np.array(yaml_file['dist_coeff'])
    
img = cv2.imread('calibration_images/tello_image2.jpg')
cv2.imshow('original', img)
    
def undistort_img(img, matrix, dist):
    """Undistort an image using the calibration matrix and distortion coefficients

    Args:
        img (np.array): Image to undistort
        matrx (np.array): Calibration matrix
        dist (np.array): Distortion coefficients

    Returns:
        np.array: Undistorted image
    """
    unwarped = cv2.undistort(img, matrix, dist, None, matrix)
    cv2.imshow('undistorted', unwarped)
    return unwarped
undistorted = undistort_img(img, camera_matrix, dist_coeff)
cv2.imshow('undistorted', undistorted)
cv2.waitKey(0)

    
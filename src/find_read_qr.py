import cv2
import numpy as np


def find_and_read_QR_MULTI(img):
    gray = img.copy()
    gray = preProcess(img)
    #look for qr code in image and read it
    detect = cv2.QRCodeDetector()
    # try:
    ret_val, values, points_list, straight_qrcodes = detect.detectAndDecodeMulti(gray)
    values = list(values)
    if ret_val:
        if len(values) == 1:
            print("Single QR code found")
            value = values[0]
            corners = []
            if value != "":
                #Draw the detected corners on qr code
                for pt in points_list[0]:
                    pt = np.array([int(pt[0]), int(pt[1])])
                    corners.append(pt)
                    cv2.circle(img, pt, 5, (0,0,255), -1)
                #Draw the value of the qr code by the center
                center = np.sum(corners, axis=0) / len(corners)
                center = center.astype(int)
                cv2.putText(img, value, center, cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 3)
                print(value)
        else:
            print("Multiple QR codes found")
            for i in range(len(values)-1):
                print(i)
                value = values[i]
                points = points_list[i]
                corners = []
                
                if value != "":
                    print("QR code found")
                    #Draw the detected corners on qr code
                    for pt in points:
                        pt = np.array([int(pt[0]), int(pt[1])])
                        corners.append(pt)
                        cv2.circle(img, pt, 5, (0,0,255), -1)
                    #Draw the value of the qr code by the center
                    center = np.sum(corners, axis=0) / len(corners)
                    center = center.astype(int)
                    cv2.putText(img, value, center, cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 3)
                    print(value)
                else:
                    print("No QR code found")
# except:
#         print("----------ERROR FOUND IN CV2 FUNCTION!--------- (Or I'm dumb lol, 50-50)")
    return img

def find_and_read_QR_SINGLE(img):
    gray = img.copy()
    gray = preProcess(img)
    #look for qr code in image and read it
    detect = cv2.QRCodeDetector()
    try:
        value, points, straight_qrcode = detect.detectAndDecode(gray)
        corners = []
        if value != "":
            print("QR code found")
            #Draw the detected corners on qr code
            for pt in points[0]:
                pt = np.array([int(pt[0]), int(pt[1])])
                corners.append(pt)
                cv2.circle(img, pt, 5, (0,0,255), -1)
            #Draw the value of the qr code by the center
            center = np.sum(corners, axis=0) / len(corners)
            center = center.astype(int)
            cv2.putText(img, value, center, cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 3)
            print(value)
        else:
            print("No QR code found")
    except:
        print("----------ERROR FOUND IN CV2 FUNCTION!--------- (Or I'm dumb lol, 50-50)")
    return img

def preProcess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    return gray

cam = cv2.VideoCapture(0)

while cv2.waitKey(1) != 27: #Press esc key to exit
    img = cam.read()[1]
    img = find_and_read_QR_MULTI(img)
    cv2.imshow('img', img)
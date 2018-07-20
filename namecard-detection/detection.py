# OpenCV implement namecard detection
import numpy as np
import cv2

def auto_scan_image_via_webcam():
    
    try:
        cam = cv2.VideoCapture(0) # load camera
    except:
        print('Cannot load Camera')

    # keep running before hit ESC
    while True:
        rect, frame = cam.read() # keep getting the frame from the cam
        if not rect:
            print('Cannot load Camera')
            break
        
        k = cv2.waitKey(10)
        if k == 27:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        edged = cv2.Canny(gray, 75, 200)

        print('Edge Detection')

        (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
        
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            screenCnt = []

            if len(approx) == 4:
                contourSize = cv2.contourArea(approx)
                # Logic for remove unnecessary rect. only detect if object is more than 10% of screen
                camSize = frame.shape[0] * frame.shape[1] # mutiply of frames width/height = cam size
                ratio = contourSize / camSize
                print(contourSize)
                print(camSize)
                print(ratio)

                if ratio > 0.1: # over 10%
                    screenCnt = approx
                break

        # if fail to get outline show original screen
        if len(screenCnt) == 0:
            cv2.imshow("WebCam", frame)
            continue
        else: # shows outline using drawContours
            print("Find contour of paper")

            cv2.drawContours(frame, [screenCnt], -1, (0, 255, 0), 2)
            cv2.imshow("WebCam", frame)

    cam.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__ == '__main__':
    auto_scan_image_via_webcam()
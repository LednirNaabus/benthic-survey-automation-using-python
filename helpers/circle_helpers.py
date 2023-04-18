from lib.common import *

def detect_circle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                                        param1=50, param2=30, minRadius=0, maxRadius=0)
    detected_circles = np.uint16(np.around(circles))
    for (x, y, r) in detected_circles[0, :]:
        cv2.circle(image, (x, y), r, (0,0,0), 3)
        cv2.circle(image, (x, y), 2, (255,0,0), 3)
    return image

def calculate_percentage():
    pass 
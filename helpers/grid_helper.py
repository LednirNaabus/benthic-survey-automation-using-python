from lib.common import *

def detect_grid(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    color = (255,255,0)
    thickness = 2
    lines_list = []
    lines = cv2.HoughLinesP(
        edges,
        1,
        np.pi/180,
        threshold=30,
        minLineLength=5,
        maxLineGap=10
    )

    for points in lines:
        x1, y1, x2, y2 = points[0]
        cv2.line(image, (x1, y1), (x2,y2), color, thickness)
        lines_list.append([(x1,y1), (x2, y2)])
    return image
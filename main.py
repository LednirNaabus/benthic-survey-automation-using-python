import cv2
import numpy as np

MAX_ROWS = 5
MAX_COLS = 5
CELL_SIZE = MAX_ROWS * MAX_COLS

class Grid:
    def __init__(self, rows=None, cols=None):
        self.rows = rows
        self.cols = cols
        self.color = (0,0,0)
        self.thickness = 1

    def define_grid(self, image):
        height, width, _ = image.shape
        cell_height = height // self.rows
        cell_width = width // self.cols
        return cell_height, cell_width
    
    def draw_grid(self, image):
        # from OpenCV
        # height = img.shape[0]
        # width = img.shape[1]
        # channels = img.shape[2]
        cell_h, cell_w = self.define_grid(image)
        for x in np.linspace(start=cell_w, stop=image.shape[1]-cell_h, num=self.cols-1):
            x = int(round(x))
            cv2.line(image, (x,0), (x, image.shape[0]), color=self.color, thickness=self.thickness)
        
        for y in np.linspace(start=cell_h, stop=image.shape[0]-cell_w, num=self.rows-1):
            y = int(round(y))
            cv2.line(image, (0, y), (image.shape[1], y), color=self.color, thickness=self.thickness)
        
        return image

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

def main():
    file = cv2.imread('circle1.png')
    im = file.copy()
    circles = detect_circle(im)

    grid = Grid(5,5)
    h, w = grid.define_grid(im)
    drawned = grid.draw_grid(circles)
    detect_grid_ = detect_grid(im)
    
    cv2.namedWindow("IMAGE OUTPUT", cv2.WINDOW_NORMAL)
    cv2.imshow("IMAGE OUTPUT", detect_grid_)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    """
    - detect circles in an image
    - calculate % of coverage
    - 
    """
    main()


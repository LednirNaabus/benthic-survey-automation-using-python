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

def preprocess(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def detect_circle(image, g):
    blur = cv2.GaussianBlur(g, (5, 5), 0)
    detected = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
    if detected is not None:
        detected = np.round(detected[0, :]).astype("int")
        for (x, y, r) in detected:
            cv2.circle(image, (x, y), r, (0, 255, 0), 2)
    return image

def calculate_percentage(circles, cell_height, cell_width):
    if circles is not None:
        for circle in circles[0]:
            x, y, r = circle
            for i in range(MAX_ROWS):
                for j in range(MAX_COLS):
                    cell_x = j * cell_width + cell_width // 2
                    cell_y = i * cell_height + cell_height // 2
                    dist = np.sqrt((x - cell_x) ** 2 + (y - cell_y) ** 2)
                    if dist < r:
                        coverage = dist/r
    return coverage

if __name__ == "__main__":
    """
    - detect circles in an image
    - calculate % of coverage
    - 
    """
    im = cv2.imread('circle1.png')
    circles = detect_circle(im, preprocess(im))

    grid = Grid(5,5)
    h, w = grid.define_grid(im)
    drawned = grid.draw_grid(circles)
    coverage = calculate_percentage(circles, h, w)
    print(f'{coverage: .2%}')
    
    cv2.namedWindow("IMAGE OUTPUT", cv2.WINDOW_NORMAL)
    cv2.imshow("IMAGE OUTPUT", drawned)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


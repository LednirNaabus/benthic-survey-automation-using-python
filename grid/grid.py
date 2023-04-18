from lib.common import *

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
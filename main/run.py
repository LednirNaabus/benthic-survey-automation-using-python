import grid as g
from helpers import *

def main():
    # general_helpers.read_file('circle1.png')
    image_file = general_helpers.read_file('circle1.png')
    circles = detect_circle(image_file)

    grid = g.Grid(5,5)
    h, w = grid.define_grid(image_file)
    drawned = grid.draw_grid(circles)
    detect_grid_ = grid.detect_grid(image_file)

    cv2.namedWindow("IMAGE OUTPUT", cv2.WINDOW_NORMAL)
    cv2.imshow("IMAGE OUTPUT", detect_grid_)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
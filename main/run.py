import grid as g
from helpers import *

def main():
    # general_helpers.read_file('circle1.png')
    image_file = general_helpers.read_file('circle1.png')
    circles_detected = detect_circle(image_file)

    grid = g.Grid(5,5)
    grid.define_grid(image_file)
    grid.draw_grid(circles_detected)
    numbered = grid.number_cellsY(circles_detected)

    cv2.namedWindow("IMAGE OUTPUT", cv2.WINDOW_NORMAL)
    cv2.imshow("IMAGE OUTPUT", numbered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
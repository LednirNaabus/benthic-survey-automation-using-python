import grid as g
from helpers import *

def main():
    image_file = general_helpers.read_file('circle1.png')
    detected_circles = detect_circle(image_file)

    grid = g.Grid(5,5)
    grid.define_grid(image_file)
    grid.draw_grid(image_file)
    grid.number_cellsY(image_file)

    num_of_cells = grid.num_cells

    # estimate percentage of coverage
    pct = estimate_percentage(detected_circles, image_file, num_of_cells)
    print(f"Percentage of coverage: {pct[0]:.2f}%")

    cv2.namedWindow("IMAGE OUTPUT", cv2.WINDOW_NORMAL)
    cv2.imshow("IMAGE OUTPUT", image_file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
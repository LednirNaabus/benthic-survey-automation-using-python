from lib.common import *

def detect_circle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                                        param1=50, param2=30, minRadius=0, maxRadius=0)
    detected_circles = np.uint16(np.around(circles))
    for (x, y, r) in detected_circles[0, :]:
        cv2.circle(image, (x, y), r, (0,0,0), 2)
        cv2.circle(image, (x, y), 2, (255,0,0), 2)
    return detected_circles

def estimate_percentage(detected_circles, image, num_cells):
    cell_width = image.shape[1] // num_cells
    cell_height = image.shape[0] // num_cells

    # iterate over each circle detected in the image
    # and calculate the number of grid cells it covers
    circle_coverage = []
    for circle in detected_circles:
        circle_x, circle_y, circle_radius = circle[0]
        # calculate the range of grid cells covered by the circle
        start_col = circle_x // cell_width
        end_col = (circle_x + circle_radius) // cell_width
        start_row = circle_y // cell_height
        end_row = (circle_y + circle_radius) // cell_height

        # calculate the number of grid cells covered
        num_covered_cells = (end_col - start_col + 1) * (end_row - start_row +1)
        circle_coverage.append(num_covered_cells)

    total_cells = num_cells ** 2
    percentages = [(covered_cells / total_cells) * 100 for covered_cells in circle_coverage]

    return percentages
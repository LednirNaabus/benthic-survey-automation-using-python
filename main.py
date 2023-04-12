import cv2
import numpy as np

def draw_grid(image, r, c, color=(0,0,0), thickness=1):
    h, w, _ = image.shape
    dy, dx = h // r, w // c

    for x in np.linspace(start=dx, stop=w-dx, num=c-1):
        x = int(round(x))
        cv2.line(image, (x,0), (x, h), color=color, thickness=thickness)

    for y in np.linspace(start=dy, stop=h-dy, num=r-1):
        y = int(round(y))
        cv2.line(image, (0, y), (w, y), color=color, thickness=thickness)

    return image

if __name__ == "__main__":
    im = cv2.imread('circle1.png')
    drawned = draw_grid(im, r=5, c=5)

    cv2.namedWindow("IMAGE OUTPUT", cv2.WINDOW_NORMAL)
    cv2.imshow("IMAGE OUTPUT", drawned)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

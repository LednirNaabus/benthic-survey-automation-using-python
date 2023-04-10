import numpy as np
import cv2
# from matplotlib import pyplot as plt
import pandas as pd

img = cv2.imread('test.png')

grid_size = 5

width = 128
height = 130
resized = cv2.resize(img, (width, height))

# draw the grid
for i in range(grid_size, resized.shape[0], grid_size):
    cv2.line(resized, (0, i), (resized.shape[1], i), (0, 0, 255), 2)
for i in range(grid_size, resized.shape[i], grid_size):
    cv2.line(resized, (i, 0), (i, resized.shape[0]), (0, 0, 255), 2)

plt.imshow(resized)
plt.show()

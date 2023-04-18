from lib.common import *

def convertToGray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def read_file(image_path):
    file = cv2.imread(image_path)
    img = file.copy()
    return img
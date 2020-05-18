import cv2
import numpy as np
from matplotlib import pyplot as py


# simple eg of loading and saving an image

# path 
path = r'C:\Users\ssamal\source\repos\ImageProcessing\Kolben_IO_01_01.tif'

# loading a grayscale image
img = cv2.imread(path, 0)

# Displaying a grayscale image
cv2.imshow('Kolben', img)

cv2.waitKey(0)
cv2.destroyAllWindows()